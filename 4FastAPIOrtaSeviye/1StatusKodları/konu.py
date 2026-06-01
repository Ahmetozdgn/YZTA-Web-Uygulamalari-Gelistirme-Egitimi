# FastAPI framework'ünü projeye dahil eder
# API uygulaması oluşturmak için kullanılır
from fastapi import FastAPI


# Body:
# HTTP isteğinin body (gövde) kısmından veri almak için kullanılır.
# Özellikle POST, PUT, PATCH isteklerinde JSON veri alırken işe yarar.
from fastapi import Body


# Path:
# URL içindeki path parametrelerini doğrulamak ve metadata eklemek için kullanılır.
# Örneğin: /courses/5 -> buradaki 5 bir path parametresidir.
from fastapi import Path


# Query:
# URL'deki query parametrelerini almak için kullanılır.
# Örneğin: /courses?category=development
from fastapi import Query


# HTTPException:
# API içinde manuel olarak hata fırlatmak için kullanılır.
# Örneğin veri bulunamazsa 404 hatası döndürmek için.
from fastapi import HTTPException


# Optional:
# Bir değişkenin boş (None) olabileceğini belirtir.
# Örneğin: description: Optional[str] = None
from typing import Optional


# BaseModel:
# Pydantic modelidir.
# Gelen JSON verisini doğrulamak ve tip kontrolü yapmak için kullanılır.
# FastAPI'nin en önemli yapı taşlarından biridir.
from pydantic import BaseModel


# Field:
# Model içindeki alanlara ekstra doğrulama ve metadata eklemek için kullanılır.
# Örneğin: minimum değer, maksimum uzunluk, örnek veri vs.
from pydantic import Field


# status:
# HTTP durum kodlarını sabit olarak kullanmamızı sağlar.
# Örneğin: status.HTTP_201_CREATED
# Sayı yazmak yerine anlamlı isim kullanmamızı sağlar.
from starlette import status


"""
Şimdi Mantığını Toparlayalım

| Yapı          | Ne İşe Yarar?                                    |
| ------------- | ------------------------------------------------ |
| FastAPI       | API uygulaması oluşturur                         |
| Body          | JSON body'den veri alır                          |
| Path          | URL içi parametreleri yönetir                    |
| Query         | URL query parametrelerini alır                   |
| HTTPException | Manuel hata fırlatır                             |
| Optional      | Alanın boş olabileceğini belirtir                |
| BaseModel     | Veri doğrulama modeli                            |
| Field         | Model alanlarına kısıt koyar                     |
| status        | HTTP durum kodlarını düzenli kullanmamızı sağlar |


"""