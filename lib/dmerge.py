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
        If some auxiliary records do not have properties specified in aux_props
        If differnt auxiliary records contribute different propertiess (aux_props not provided)
        If any auxiliary records do not contribute any additional properties beyond these already present in the primary record (aux_props not provided)

    Notes
    -----
    Each property from the auxiliary records is classified as "numeric" or "non-numeric".
    Numeric property values are interpolated according to the time difference between the primary record precision timestamp
    and auxiliary record precision timestamp(s).
    For non-numeric properties the record closest to the primary record in terms of precision timestamp is selected as the property source.
    """

    aux_props = validate_dmerge_args(primary, auxiliaries, aux_props)

    if len(auxiliaries) == 1:
        # TODO Simpler case where numeric properties do not have to be interpolated and the choice of "closest in time" record is obvious
    else:
        # TODO Complex case where numeric properties have to be interpolated and we need to compute which record is closest in time to the primary


def validate_dmerge_args(primary, auxiliaries, aux_props=None):
    """Utility method for validating arguments passed to dmerge() method

    Returns
    -------
    list[str]
        List of properties to merge into the primary record

    See Also
    --------
    dmerge: for information about validation errors raised by this method
    """"

    if len(auxiliaries) == 0:
        raise ValueError("Must pass at least one auxiliary record")

    if aux_props:
        for aux in auxiliaries:
            if not aux.keys().issuperset(aux_props):
                e = ValueError("Auxiliary record does not have all expected properties")
                e.expectedProps = aux_props
                e.record = aux
                raise e
    else:
        aux_props = auxiliaries[0].keys() - primary.keys()        
        
        for aux in auxiliaries:
            extra_props = aux.keys() - primary.keys()

            if len(extra_props) == 0:
                e = ValueError("Auxiliary record does not contribute any properties beyond these already in the primary record")
                e.record = auxiliaries[0]
                raise e

            if aux_props != extra_props:
                e = ValueError("Different auxiliary records contribute different properties")
                e.record1 = auxiliaries[0]
                e.record2 = aux
                raise e

    return aux_props
