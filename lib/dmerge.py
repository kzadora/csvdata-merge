import datetime

TIME_ATTR = "TIME" # Time attribute name
PRECISION_TIME_ATTR = "__PRECISION_TIME" # Precision time attribute name

MIN_TIME_DELTA = datetime.timedelta(milliseconds=1)

def dmerge(primary, auxiliaries, aux_props=None):
    """Merges data from auxiliary records into primary record

    Parameters
    ----------
    primary : dict
        The primary record
    auxiliaries : list[dict]
        The auxiliary record(s) (one or more)
    aux_props : list[str], optional
        Names of the properties from the auxiliary record(s) that need to be merged into the primary record.
        If not specified, all properties from the auxiliary records that are not present in the primary record are merged.

    Raises
    ------
    ValueError
        If there are no auxiliary records
        If some auxiliary records do not have attributes specified in aux_props
        If auxiliary records do not have the same attributes (aux_props not provided)

    Notes
    -----
    Each attribute from the auxiliary records is classified as "numeric" or "non-numeric".
    Numeric attribute values are interpolated according to the time difference between the primary record precision timestamp
    and auxiliary record precision timestamp(s).
    For non-numeric attributes the record closest to the primary record in terms of precision timestamp is selected as the attribute source.
    """

    if len(auxiliaries) == 0:
        raise ValueError("Must pass at least one auxiliary record")

    if aux_props:
        # TODO: verify that all auxiliary records have all attributes specified by aux_props
        pass
    else:
        # TODO: verify that all auxiliary records have the same set of attributes
        pass