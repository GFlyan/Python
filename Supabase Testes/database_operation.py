from data.connect import supabase


def insert(codeSerie: str, userEmail: str, checkType: str):
    if not codeSerie or not userEmail or not checkType:
        raise ValueError('Dados insuficientes.')

    try:
        # Tentativa de inserção
        response = (
            supabase.table("series")
            .insert({
                "code_serie": codeSerie,
                "user_email": userEmail,
                "check_type": checkType
            })
            .execute()
        )

        return response.data  # Dados inseridos com sucesso

    except Exception as error:
        raise error