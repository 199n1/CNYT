# Librería de números complejos( Natalia Mahecha )
# Representación cartesiana: (a, b) donde a=parte real, b=parte imaginaria
# Representación polar: (r, θ) donde r=módulo, θ=fase (en radianes)

import math


def suma(z1, z2):
    """Suma de dos números complejos"""
    return (z1[0] + z2[0], z1[1] + z2[1])

def resta(z1, z2):
    """Resta de dos números complejos"""
    return (z1[0] - z2[0], z1[1] - z2[1])

def producto(z1, z2):
    """Producto de dos números complejos"""
    real = z1[0]*z2[0] - z1[1]*z2[1]
    imag = z1[0]*z2[1] + z1[1]*z2[0]
    return (real, imag)

def division(z1, z2):
    """División de dos números complejos"""
    denom = z2[0]**2 + z2[1]**2
    if denom == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    real = (z1[0]*z2[0] + z1[1]*z2[1]) / denom
    imag = (z1[1]*z2[0] - z1[0]*z2[1]) / denom
    return (real, imag)

def modulo(z):
    """Módulo de un número complejo"""
    return math.sqrt(z[0]**2 + z[1]**2)

def conjugado(z):
    """Conjugado de un número complejo"""
    return (z[0], -z[1])

def cartesiano_a_polar(z):
    """Conversión de cartesiano a polar"""
    r = modulo(z)
    theta = math.atan2(z[1], z[0])
    return (r, theta)

def polar_a_cartesiano(p):
    """Conversión de polar a cartesiano"""
    r, theta = p
    return (r*math.cos(theta), r*math.sin(theta))

def fase(z):
    """Fase de un número complejo (en radianes)"""
    return math.atan2(z[1], z[0])
