CREATE TABLE IF NOT EXISTS dolar_cotizaciones
(
    id           integer primary key AUTO_INCREMENT,
    dolar_nacion REAL,
    M_ArUSD      REAL,
    M1_ArUSD     REAL,
    M2_ArUSD     REAL,
    M3_ArUSD     REAL,
    M4_ArUSD     REAL
);
-- Tabla con las cotizaciones sacadas de Bloomberg
CREATE TABLE IF NOT EXISTS bloomberg_cotizaciones
(
    id                            integer primary key AUTO_INCREMENT,
    WTI_NYMEX_M1_USD_bbl_price    REAL,
    WTI_NYMEX_M1_USD_bbl_change   REAL,
    BRENT_NYMEX_M2_USD_bbl_price  REAL,
    BRENT_NYMEX_M2_USD_bbl_change REAL,
    RBOB87_M1_cpg_price           REAL,
    RBOB87_M1_cpg_change          REAL,
    Heating_Oil_M1_cpg_price      REAL,
    Heating_Oil_M1_cpg_change     REAL
);

-- Tabla con los datos de "Dated Brent" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_dated_brent
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_bbl  REAL,
    M1_USD_bbl REAL,
    M2_USD_bbl REAL,
    M3_USD_bbl REAL,
    M4_USD_bbl REAL,
    M5_USD_bbl REAL
);

-- Tabla con los datos de "ICE Brent" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_ice_brent
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_bbl  REAL,
    M1_USD_bbl REAL,
    M2_USD_bbl REAL,
    M3_USD_bbl REAL,
    M4_USD_bbl REAL,
    M5_USD_bbl REAL
);

-- Tabla con los datos de "WTI" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_wti
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_bbl  REAL,
    M1_USD_bbl REAL,
    M2_USD_bbl REAL,
    M3_USD_bbl REAL,
    M4_USD_bbl REAL,
    M5_USD_bbl REAL
);

-- Tabla con los datos de "CME RBOB87" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_cme_rbob87
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "HO" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_ho
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "Jet54 USGC" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_jet54_usgc
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "FO NY" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_fo_ny
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "Propane OPIS" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_propane_opis
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "Butane OPIS" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_butane_opis
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);

-- Tabla con los datos de "Naphtha CIF NWE" sacados de CME
CREATE TABLE IF NOT EXISTS cme_cotizaciones_naphtha_cif_nwe
(
    id         integer primary key AUTO_INCREMENT,
    M_USD_Gal  REAL,
    M1_USD_Gal REAL,
    M2_USD_Gal REAL,
    M3_USD_Gal REAL,
    M4_USD_Gal REAL,
    M5_USD_Gal REAL
);