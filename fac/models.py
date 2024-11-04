from django.db import models
from bases.models import ClaseModelo, ClaseModelo2 

from inv.models import Producto

class Cliente(ClaseModelo):
    NAT = 'Natural'
    JUR = 'Juridica'
    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Juridica')
    ]

    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.apellidos, self.nombres)

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "clientes"

class FacturaEnc(ClaseModelo2):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __srt__(self):
        return '{}'.formt(self.id)
    
    def save(self):
        self.total=self.sub_total - self.descuento
        super(FacturaEnc,self).save() 

    class meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"

class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self, *args, **kwargs):
        self.sub_total = float(self.cantidad) * self.precio
        self.total = self.sub_total - self.descuento
        super(FacturaDet, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name = "Detalle Factura"