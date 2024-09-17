# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class NguoiDung(Base):
    __tablename__ = 'nguoi_dung'

    nguoi_dung_id = Column(Integer, primary_key=True)
    email = Column(String(255))
    mat_khau = Column(String(255))
    ho_ten = Column(String(255))
    tuoi = Column(Integer)
    anh_dai_dien = Column(String(255))
    refresh_token = Column(Text)


class HinhAnh(Base):
    __tablename__ = 'hinh_anh'

    hinh_id = Column(Integer, primary_key=True)
    ten_hinh = Column(String(255))
    duong_dan = Column(String(255))
    mo_ta = Column(String(255))
    nguoi_dung_id = Column(ForeignKey('nguoi_dung.nguoi_dung_id'), index=True)

    nguoi_dung = relationship('NguoiDung')


class BinhLuan(Base):
    __tablename__ = 'binh_luan'

    binh_luan_id = Column(Integer, primary_key=True)
    nguoi_dung_id = Column(ForeignKey('nguoi_dung.nguoi_dung_id'), index=True)
    hinh_id = Column(ForeignKey('hinh_anh.hinh_id'), index=True)
    ngay_binh_luan = Column(Date)
    noi_dung = Column(String(255))

    hinh = relationship('HinhAnh')
    nguoi_dung = relationship('NguoiDung')


class LuuAnh(Base):
    __tablename__ = 'luu_anh'

    nguoi_dung_id = Column(ForeignKey('nguoi_dung.nguoi_dung_id'), index=True)
    hinh_id = Column(ForeignKey('hinh_anh.hinh_id'), index=True)
    ngay_luu = Column(Date)
    luu_anh_id = Column(Integer, primary_key=True)

    hinh = relationship('HinhAnh')
    nguoi_dung = relationship('NguoiDung')
