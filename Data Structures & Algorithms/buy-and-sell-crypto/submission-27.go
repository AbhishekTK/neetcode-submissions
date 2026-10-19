func maxProfit(prices []int) int {
	r,minb := 0,prices[0]

	for _,sell := range prices {
		if sell -minb >r{
			r = sell-minb
		}
		if sell<minb{
			minb = sell
		}
	}
	return r

}
