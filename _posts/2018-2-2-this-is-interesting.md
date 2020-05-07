---
layout: post
title: With syntax highlighting
author: Ajit
updated: 2019-7-27 12:00:00 +0530
og-image-ext: https://source.unsplash.com/mlEWD6uFCzI/1600x900
categories:
  - web
---

Check this one for an example on using OpenGraph images per post.

Next you can update your site name, avatar and other options using the _config.yml file in the root of your repository (shown below).

{% highlight javascript %}
const test1 = () => {
  console.log("Syntax highlighting");
};

const test2 = () => {
  console.log("Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus doloribus a atque corporis quisquam. Quidem, enim accusantium quas voluptates molestiae quaerat accusamus saepe possimus eum iste? Quo voluptatem minus neque?");
};
{% endhighlight %}

Directly placing the link like this doesn't work:
https://source.unsplash.com/mlEWD6uFCzI/1600x900

> `overflow-wrap: break-word` allows for this 👆link to break into the next line.

# This is an <h1> tag
## This is an <h2> tag
### This is an <h3> tag
#### This is an <h4> tag
##### This is an <h5> tag
###### This is an <h6> tag

*This text will be italic*

_This will also be italic_

**This text will be bold**

__This will also be bold__

_You **can** combine them_

~~This is for strike-through~~

### Unordered

- Item 1
* Item 2
  * Item 2a
  + Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

### Image

![Image from Unsplash](https://source.unsplash.com/mlEWD6uFCzI/1600x900)
*Image credits: Unsplash*

[Link to GitHub](http://github.com)

> Blockquotes
>
> Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus doloribus a atque corporis quisquam. Quidem, enim accusantium quas voluptates molestiae quaerat accusamus saepe possimus eum iste? Quo voluptatem minus neque?

You can also use `inline code`.

### Here's a table

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

First Header | Second Header | Third Header
------------ | ------------- | -------------
Content from cell 1 | Content from cell 2 | Content from cell 3
Content in the first column | Content in the second column | Content in the third column
