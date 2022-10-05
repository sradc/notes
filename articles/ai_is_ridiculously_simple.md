# AI is ridiculously simple

Many of the current state of the art AI models
are far simpler than they have any right to be, 
given the results they produce.

I tried out GitHub Copilot recently, 
and to be honest had a few holy shit moments.
It's not perfect, but it's pretty damn good.
And this technology is only going to get better.

But how was the model trained?
- Download a giant lump of text (the whole of wikipedia and then some)
- Give the model a piece of text, and train it to predict the next word
- Keep doing this until the model is good enough

This gives you a general purpose language model, 
that can generate text (by predicting the next word again and again).
To go from this to Copilot:
- Take the model from before.
- Download a bunch of code samples
- Give the model a batch of code samples at a time, and train it to predict the next line
- Keep doing this until the model is good enough

Ta-dah, you have fine-tuned a language model, 
and turned it into a code completion model.

But what about the internal logic of the model? Surely that's complicated?






