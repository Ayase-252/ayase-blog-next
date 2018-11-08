function delay (fn, time) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      fn(resolve, reject)
    }, time)
  })
}

export { delay }
