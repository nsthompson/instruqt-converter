import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import log as requests_logger
from gql.transport.exceptions import TransportQueryError


requests_logger.setLevel(logging.WARNING)


class API():
    def __init__(self, config):
        self.config = config

        _headers = {
            "Authorization": "Bearer " + self.config.INSTRUQT_API_KEY
        }

        _transport = RequestsHTTPTransport(
            url=self.config.INSTRUQT_API_URL,
            headers=_headers,
            use_json=True
            )
        self.client = Client(
            transport=_transport,
            fetch_schema_from_transport=True
            )

    def graphql_query(self, query_type, slug):
        if query_type == "track":
            query = gql("""
                query($trackSlug:String!, $orgSlug:String!) {
                    track(trackSlug:$trackSlug, organizationSlug:$orgSlug) {
                        id
                        slug
                        challenges {
                            id
                            slug
                        }
                    }
                }""")

            variables = {
                "trackSlug": slug,
                "orgSlug": self.config.INSTRUQT_ORG_SLUG
            }

            try:
                result = self.client.execute(query, variable_values=variables)
            except TransportQueryError as transport_error:
                result = transport_error.data

            return result
