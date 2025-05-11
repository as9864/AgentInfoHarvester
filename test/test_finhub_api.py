from infoharvester.fundamentals.finhub_api import fetch_company_profile, fetch_financials

def test_finhub():
    profile = fetch_company_profile("AAPL")
    metrics = fetch_financials("AAPL")

    print("📄 Company Profile:")
    print(f"Name: {profile.get('name')}")
    print(f"Sector: {profile.get('finnhubIndustry')}")
    print(f"CEO: {profile.get('ceo')}")
    print(f"Web: {profile.get('weburl')}")

    print("\n📊 Financial Metrics:")
    print(f"Revenue: {metrics.get('revenuePerShareTTM')}")
    print(f"Net Profit Margin: {metrics.get('netProfitMarginTTM')}")
    print(f"ROE: {metrics.get('roeTTM')}")
    print(f"Debt to Equity: {metrics.get('totalDebt/totalEquity')}")

if __name__ == "__main__":
    test_finhub()