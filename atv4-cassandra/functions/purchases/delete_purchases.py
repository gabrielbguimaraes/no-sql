from uuid import UUID
from utils.utils_users import get_user
from utils.utils_purchase import get_purchase

def delete_purchase(session, purchase_id):

    try:
        purchase = get_purchase(session, UUID(purchase_id))

        if purchase is None:
            print("Compra não encontrada")
            return
        
        user = get_user(session, purchase.user_id)
        if user is None:
            print("Usuário não encontrado")
            return
        
        user_compras = list(user.compras) if user.compras else []
        user_compras =[ compra for compra in user_compras if compra["id"] != str(purchase.id) ]

        script = """
            UPDATE user
            SET compras = %s
            WHERE id = %s
        """

        session.execute(
            script,
            (
                user_compras,
                user.id,
            )
        )

        delete_row = """
            DELETE FROM purchase
            WHERE id = %s
        """

        session.execute(delete_row, (purchase.id,))

        print("Compra deletada com sucesso!")
        return
    except Exception as e:
        print(f"Erro ao deletar compra: {e}")
        return None
        
