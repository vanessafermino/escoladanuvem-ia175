def registrar_notas():
    notas = []

    print("Digite as notas da turma (0 a 10). Digite 'fim' para encerrar.")

    while True:
        entrada = input("Nota: ").strip().lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número ou 'fim' para encerrar.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n✅ Média da turma: {media:.2f}")
    else:
        print("\n⚠️ Nenhuma nota válida foi registrada.")

# Executa o programa
registrar_notas()