import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class Book:
    title: str
    author: str
    price: int

@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return Book(title="The Godfather", author="Mario Puzo", price=750)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str, price:int) -> Book:
        print(f'Adding {title} by {author}')

        return Book(title=title, author=author, price=price)

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/book", graphql_app)

#app.add_websocket_route("/book", graphql_app)
