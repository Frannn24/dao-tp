CREATE TABLE Libros (
    Codigo INTEGER PRIMARY KEY,
    Titulo TEXT NOT NULL,
    PrecioReposicion REAL,
    Estado TEXT NOT NULL
);

CREATE TABLE Socios (
    Numero INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL
);

CREATE TABLE Prestamos (
    ID INTEGER PRIMARY KEY,
    LibroCodigo INTEGER,
    SocioNumero INTEGER,
    FechaPrestamo DATE NOT NULL,
    FechaDevolucion DATE,
    DiasRetraso INTEGER,
    FOREIGN KEY (LibroCodigo) REFERENCES Libros(Codigo),
    FOREIGN KEY (SocioNumero) REFERENCES Socios(Numero)
);

CREATE TABLE Extravios (
    LibroCodigo INTEGER,
    FechaExtravio DATE,
    FOREIGN KEY (LibroCodigo) REFERENCES Libros(Codigo)
);

