#!/usr/bin/env python
# coding: utf-8

# <h1>Biodata</h1>

# In[6]:


nama = input ('Nama :')
umur = input('Umur :')
tanggal_lahir = input ('Tanggal Lahir :')
alamat = input ('Alamat :')
hobi = input ('Hobi :')
cita_cita = input ('Cita - cita :')

biodata = nama, int(umur),int(tanggal_lahir),alamat,hobi,cita_cita
print(biodata)

