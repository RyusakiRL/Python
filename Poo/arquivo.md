# Diagrama de caso e uso

```mermaid
classDiagram
    class Livro {
        +String titulo
        +String autor
        +String assunto
        +verificarDisponibilidade()
    }
    class Exemplar {
        +int codigo_identificador
        +bool emprestado
    }
    class Usuario {
        +String nome
        +int id_academico
        +solicitarEmprestimo()
        +reservarLivro()
    }

    Livro "1" -- "1..*" Exemplar : possui
    Usuario "1" -- "0..*" Exemplar : empresta
    Usuario "1" -- "0..*" Livro : reserva