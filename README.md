# notes

### 2022-10-05 text-to-video

<img src="./media/Make-A-Video_dog.jpg" width=200>

As if all the text-to-image models released in the last year weren't exciting enough, we've moved on to fairly high quality text-to-video already:
- https://imagen.research.google/video/ (released today, 2022-10-05)
- https://phenaki.github.io/ (released today, 2022-10-05)
- https://ai.facebook.com/blog/generative-ai-text-to-video/ (last week, 2022-09-29)

### 2022-10-05 playing with copilot

Decided to give [copilot](https://github.com/features/copilot) a try this evening.
Set out to see how it works, on a toy example of hyperparameter tuning.

It was doing fairly well at generating code 
(although I'm still getting the hang of "prompting it" such 
that it produces the desired output), 
and it then surprised me with a `#TODO`, 
telling me to use a library instead of coding this stuff myself 😮😂.
 
The code snippet:

```python
scores = []
for width in hyperparams["width"]:
    for depth in hyperparams["depth"]:
        score = train_model(width=width, depth=depth)
        scores.append((score, width, depth))
scores.sort(reverse=True)
best_score, best_width, best_depth = scores[0]
print(f"Best score: {best_score}, width: {best_width}, depth: {best_depth}")

# TODO: Use a library like scikit-learn to do this more easily
# https://scikit-learn.org/stable/modules/grid_search.html
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html
```

Update: More stuff copilot has come up with:

```python
# I’m not sure if this is the best way to do this, but it works. 
# I’m using optuna to plot the results, 
# but you could use any plotting library you want.
```

Seems to be constantly questioning my approach...
Maybe it has a point 😅? 

Update: added the result of my first play with copilot in [dump/2022-10-05_copilot_first_try.py](dump/2022-10-05_copilot_first_try.py).

Very impressed... I think this is a big deal.
Although I had seen it mentioned, and discussed,
I hadn't quite appreciated how impactful this kind of tool
is probably going to be.
I have a feeling that the majority of people are currently in that boat;
they've seen mention, or talk of copilot, 
but haven't looked into it much.

Some cool things:
- I've never used `plotly.express`, and just told github copilot to use it via a comment. After a few tries it produced working code
- I was able to get copilot to transform the data fairly easily, using comments
- it produced the `iter_param_combos` code (had to nudge it to use `product`)
- it produced the evaluation loop
- it produced the plotting code

There was a certain amount of nudging; trying different starting points (fragments of code, comments); but even in that tiny example copilot did a lot.

I even found that it could suggest better function names. 
I just added `# a better name for this function would be`
above the functions, and it suggested the names that are currently used... Amazing.

---

# Links and resources

### [heejkoo/Awesome-Diffusion-Models](https://github.com/heejkoo/Awesome-Diffusion-Models)
- "A collection of resources and papers on Diffusion Models and Score-matching Models, a darkhorse in the field of Generative Models"


### [CarperAI/FIM-NeoX-1.3B](https://huggingface.co/CarperAI/FIM-NeoX-1.3B)
- large-scale infilling-enabled autoregressive language model (first of a series)


### [InCoder: A Generative Model for Code In-Filling and Synthesis](https://sites.google.com/view/incoder-code-models)
- a generative, decoder-only Transformer using a causal-masking training objective, which trains a model to generate entire code files in arbitrary orderings via masking
- [huggingface demo](https://www.google.com/url?q=https%3A%2F%2Fhuggingface.co%2Fspaces%2Ffacebook%2Fincoder-demo&sa=D&sntz=1&usg=AOvVaw3IcuVBoMRILHeMyx_pLFgO)


### [github.com/karpathy/makemore](https://github.com/karpathy/makemore/blob/master/makemore.py)
- char language model
- includes char-level transformer
- [video series](https://www.youtube.com/watch?v=PaCmpygFfXo) being created that goes with it


### [Optuna tutorial](https://optuna.readthedocs.io/en/stable/tutorial/index.html)
- includes a tutorial video
- "Optuna is an automatic hyperparameter optimization software framework, particularly designed for machine learning"


### [Hands-on Machine Learning Notebooks, 3rd edition](https://github.com/ageron/handson-ml3)
- Jupyter notebooks for *Hands-on Machine Learning with Scikit-Learn, Keras and TensorFlow*
- Packed full of useful information


### [MLOps with Vertex AI repo](https://github.com/GoogleCloudPlatform/mlops-with-vertex-ai)
- implements the end-to-end MLOps process using Vertex AI platform and Smart Analytics 
- uses Keras to implement the ML model, TFX to implement the training pipeline, and Model Builder SDK to interact with Vertex AI.


### [Whisper: a neural net that approaches human level robustness and accuracy on English speech recognition](https://openai.com/blog/whisper/)
- [repo](https://github.com/openai/whisper)
- [paper pdf](https://cdn.openai.com/papers/whisper.pdf)


### [DreamBooth Stable Diffusion training in 10 GB VRAM, using xformers, 8bit adam, gradient checkpointing and caching latents.](https://old.reddit.com/r/MachineLearning/comments/xtc3g5/d_dreambooth_stable_diffusion_training_in_10_gb/)
- [code](https://github.com/ShivamShrirao/diffusers/tree/main/examples/dreambooth)
- [Colab notebook](https://colab.research.google.com/github/ShivamShrirao/diffusers/blob/main/examples/dreambooth/DreamBooth_Stable_Diffusion.ipynb)


### [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/)
- "This is a gentle introduction to how Stable Diffusion works."
- [Hacker News discussion](https://news.ycombinator.com/item?id=33084205)


### [Imagen Video: high definition video generation with diffusion models](https://imagen.research.google/video/)
- Given a text prompt, Imagen Video generates high definition videos using a base video generation model and a sequence of interleaved spatial and temporal video super-resolution models
- [Hacker News discussion](https://news.ycombinator.com/item?id=33098704)
- [Paper pdf](https://imagen.research.google/video/paper.pdf)


### [CMSC 430: Design and Implementation of Programming Languages](https://www.cs.umd.edu/class/fall2022/cmsc430/index.html)

<img src="./media/wizard.jpg" width=200>

- an introduction to compilers.
- tries to give students the ability to design, implement, and extend a programming language. 
- [Hacker News discussion](https://news.ycombinator.com/item?id=33093666)


### [SOLID Principles explained in Python with examples.](https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd)

<img src="./media/solid_principles.jpg" width=400>

- Contains straightforward Python examples for SOLID:
    - Single Responsibility Principle
    - Open-Closed Principle
    - Liskov Substitution Principle
    - Interface Segregation Principle
    - Dependency Inversion Principle


### [ZenML](https://zenml.io/home)
- "Open-source pipeline framework"
- "Get all your ML workflows running on any tooling stack with minimum effort."
