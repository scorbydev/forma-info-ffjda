def compute_license_status(
    season: str,
    current_season: str,
    payment_status: str,
    certificate_valid: bool,
    mutation_pending: bool = False,
) -> str:
    """Retourne le statut metier d'une licence.

    Bug pedagogique volontaire: la saison est testee trop tot. Le correctif
    attendu consiste a appliquer l'ordre metier documente dans expected_fix.md.
    """
    if season != current_season:
        return "EXPIRED_SEASON"
    if payment_status != "PAID":
        return "PENDING_PAYMENT"
    if certificate_valid is False:
        return "PENDING_CERTIFICATE"
    if mutation_pending is True:
        return "PENDING_MUTATION"
    return "ACTIVE"

