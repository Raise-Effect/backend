from functools import lru_cache
from . import models


def lru_jsonify_cache(**kwargs):
    # TODO: Implemementation broken
    raise NotImplemented
    @lru_cache(**kwargs)
    def f(*params, **kwargs):
        return jsonify()
    return lru_cache(**kwargs)(f)


@lru_jsonify_cache()
def construct_county(fips, expand_fields):
    county = models.County.query.filter_by(fips=fips).first()
