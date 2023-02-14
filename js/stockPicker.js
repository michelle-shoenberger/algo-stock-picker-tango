exports.picker = function(prices) {
  // pointers
  let buy = 0;
  let greatest = 0; //greatest profit
  let indices = [0,0]; // track indices to return
  // loop through stocks
  for (let i=0; i<prices.length; i++) {
    if (prices[i] < prices[buy]) {
      buy = i
    } else if (prices[i] - prices[buy] > greatest) {
      greatest = prices[i] - prices[buy]
      indices = [buy, i]
    }
  }
  return indices

}
