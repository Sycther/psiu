from unittest import result
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://api-us-east-1.graphcms.com/v2/ckzn0i50h55rt01yy2hsf9tdg/master")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

queryBrothers = gql(
    """    
    query MyQuery {
        brotherList(where: {name: "ourBrotherOrder"}) {
            brothers {
            desc
            title
            name
            bio
            img {
                url
            }
            }
        }
    }
"""
)

queryEvents =gql(
    """
    query EventsList {
        events{
            title
            desc
            startTime
            location
            img {
                url
            }
        }
    }
    """
)