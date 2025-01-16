import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def plot_trades_chart(data, trades):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='BTC price'))

    if not trades.empty:
        buy_trades = trades[trades['Size'] > 0]
        sell_trades = trades[trades['Size'] < 0]

        fig.add_trace(go.Scatter(
            x=buy_trades['EntryTime'], y=buy_trades['EntryPrice'],
            mode='markers', name='매입',
            marker=dict(color='green', size=10, symbol='triangle-up')
        ))

        fig.add_trace(go.Scatter(
            x=sell_trades['EntryTime'], y=sell_trades['EntryPrice'],
            mode='markers', name='청산',
            marker=dict(color='red', size=10, symbol='triangle-down')
        ))

    fig.update_layout(title="BTC 매입/청산", xaxis_title="시간", yaxis_title="가격 (USDT)")
    st.plotly_chart(fig)

def plot_equity_curve(equity_curve):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=equity_curve.index, y=equity_curve['Equity'], mode='lines'))
    fig.update_layout(
        title="자본 변동",  
        xaxis_title="시간", 
        yaxis_title="자산 (USD)", 
        template="plotly_white",  
        height=600  
    )
    st.plotly_chart(fig)

def plot_returns_bar_chart(trades):
    returns_by_day = trades.groupby(trades['EntryTime'].dt.date)['PnL'].sum()
    fig = px.bar(returns_by_day, x=returns_by_day.index, y='PnL', title="일일 손익")
    st.plotly_chart(fig)

def plot_comparison_chart(backtest_equity_curve, historical_data):
    """
    Plots a comparison graph between backtest performance and buy-and-hold strategy.

    Parameters:
        backtest_equity_curve (pd.DataFrame): Backtest equity curve.
        historical_data (pd.DataFrame): Historical BTC price data.
    """
    start_price = historical_data["Close"].iloc[0]
    historical_data["BuyHoldEquity"] = historical_data["Close"] / start_price * backtest_equity_curve["Equity"].iloc[0]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=backtest_equity_curve.index,
        y=backtest_equity_curve["Equity"],
        mode="lines",
        name="Backtest Equity",
        line=dict(color="blue", width=2)
    ))

    fig.add_trace(go.Scatter(
        x=historical_data["Open Time"],
        y=historical_data["BuyHoldEquity"],
        mode="lines",
        name="Buy & Hold Equity",
        line=dict(color="green", width=2, dash="dot")
    ))

    fig.update_layout(
        title="백테스팅 전략 vs. 매수 후 보류",
        xaxis_title="시간",
        yaxis_title="자산 (USD)",
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)