impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut r = 0;
        let mut minb = prices[0];
        for &sell in &prices{
            r = r.max(sell-minb);
            minb = minb.min(sell);
        }
        r
    }
}
