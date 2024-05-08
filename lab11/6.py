response = {
    'addressee': 'John Doe',
    'amount': 10,
    'product': 'widgets',
    'sender': 'Jane Smith',
    'post': 'Manager',
    'institution': 'ABC Corporation'
}

letter = """Dear Mr. {addressee}:
With reference to our telephone conversation today, I am writing to confirm your order for: {amount} x {product} (Ref. No. 856).
Please contact us again if we can help in any way.

Yours sincerely,
{sender}
{post} of {institution}"""

print(letter.format(**response))

