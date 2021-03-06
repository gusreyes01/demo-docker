from rest_framework import serializers
from .models import Cliente, Avaluo, DatosCliente, Mancomunado, Estado, Municipio, \
    ADR, ALR, Bien, Proposito, Servicio, Inmueble, DescripcionBien, Colegio, Valuador, PropuestaTecnica



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class DatosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosCliente
        fields = '__all__'


class MancomunadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancomunado
        fields = '__all__'


class ALRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ALR
        fields = '__all__'


class ADRSerializer(serializers.ModelSerializer):
    alr = ALRSerializer(many=True, read_only=True)

    class Meta:
        model = ADR
        fields = ('id', 'nombre', 'titular', 'localizacion', 'domicilio', 'alr')


class BienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bien
        fields = '__all__'


class PropositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposito
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'


class DescripcionBienSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescripcionBien
        fields = '__all__'


class AvaluoSerializer(serializers.ModelSerializer):
    # Cliente
    cliente_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                    queryset=Cliente.objects.all(),
                                                    source='cliente')
    cliente = ClienteSerializer(read_only=True)

    # Bien
    bien_id = serializers.PrimaryKeyRelatedField(required=False,
                                                 write_only=True,
                                                 queryset=Bien.objects.all(),
                                                 source='tipo_bien')
    tipo_bien = BienSerializer(read_only=True)

    # Proposito
    proposito_id = serializers.PrimaryKeyRelatedField(required=False,
                                                      write_only=True,
                                                      queryset=Proposito.objects.all(),
                                                      source='proposito')
    proposito = PropositoSerializer(read_only=True)

    # Servicio
    tipo_servicio_id = serializers.PrimaryKeyRelatedField(required=False,
                                                          write_only=True,
                                                          queryset=Servicio.objects.all(),
                                                          source='tipo_servicio')
    tipo_servicio = ServicioSerializer(read_only=True)

    # Inmueble
    tipo_inmueble_id = serializers.PrimaryKeyRelatedField(required=False,
                                                          write_only=True,
                                                          queryset=Inmueble.objects.all(),
                                                          source='tipo_inmueble')
    tipo_inmueble = InmuebleSerializer(read_only=True)

    datos_cliente = DatosClienteSerializer()
    mancomunado = MancomunadoSerializer()
    descripcion_bienes = DescripcionBienSerializer(many=True, required=False)

    fecha_asignacion = serializers.DateField(format="%d-%m-%Y",
                                             input_formats=['%d-%m-%Y', 'iso-8601'],
                                             required=False)
    fecha_compromiso = serializers.DateField(format="%d-%m-%Y",
                                             input_formats=['%d-%m-%Y', 'iso-8601'],
                                             required=False)
    fecha_solicitud_correo = serializers.DateField(format="%d-%m-%Y",
                                                   input_formats=['%d-%m-%Y', 'iso-8601'],
                                                   required=False)

    class Meta:
        model = Avaluo
        # Serialize all fields
        exclude = ()

    def create(self, validated_data):
        datos_cliente_data = validated_data.pop('datos_cliente', None)
        mancomunado_data = validated_data.pop('mancomunado', None)
        descripcion_bien_data = validated_data.pop('descripcion_bienes', None)

        avaluo = Avaluo.objects.create(**validated_data)

        if datos_cliente_data:
            DatosCliente.objects.create(avaluo=avaluo, **datos_cliente_data)
        if mancomunado_data:
            Mancomunado.objects.create(avaluo=avaluo, **mancomunado_data)

        if descripcion_bien_data:
            for descripcion_data in descripcion_bien_data:
                DescripcionBien.objects.create(avaluo=avaluo, **descripcion_data)

        return avaluo


class ColegioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colegio
        fields = '__all__'


class ValuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuador
        fields = '__all__'


class PropuestaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropuestaTecnica
        fields = '__all__'
