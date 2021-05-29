**Exercise 7 - Edge Detection!**

**Overview**

In this exercise, you will implement a very basic edge detection
algorithm - something similar to the **edge detection** mode in the
img2turtle utility we gave you! The goal of edge detection is to find
the regions of an image that have a sharp change in colour or intensity.


The algorithm produces white edges on a black background, but it is
trivial to convert it to black edges on a white background if you prefer
it that way.

 

**Image Kernels**

We will be using what are called **image kernels** to help us do this.
What is an image kernel? It is simply a (usually small) matrix that
represents what you can think of as some sort of filter. While these
kernels are very powerful in the field of image processing and are often
part of convolutional neural networks, at their core they are a very
simple idea.

 

Kernels come in all sorts of shapes and sizes and can help you apply
effects to images such as blurring, sharpening, embossing, etc. [Here is
an excellent article](https://setosa.io/ev/image-kernels/) explaining
the basics of how image kernels work, with a bunch of great interactive
visualizations.

 

Your exercise also gives you the basic setup so you can implement most
if not all of the other effects given in the article above, but we'll
only be focusing on one for the sake of this exercise. Feel free to ask
us about how to do the others if you're unsure.

 

**Sobel Operators**

We will be using a pair of `3x3` kernels (referred to as Sobel
operators) to help us perform the edge detection. The two kernels are
shown below and are often referred to as G~X~ and G~Y~. You will also
see these defined at the top in the starter file.

\

![gradients.jpeg](/courses/192878/files/11667619/preview)

\

If you look at them carefully, you can get a sense of how they work. For
instance, in G~X~ we seem to be subtracting the right side of pixels
from the left side. So, if there was a large change in colour from the
left to right, we would get a number with a large magnitude (positive or
negative). However, if the colour was the same from left to right, then
we would get a value of 0 from the kernel for the given region.
Similarly, G~Y~ looks for changes in colour from top to bottom.

\

Note that this is in some sense a special scenario since we have 2
kernels instead of one. For each pixel, we're going to get 2 values; one
from performing the multiplication with G~X~ at that pixel, and the
other from G~Y~. The question is, how do we combine these values in a
way that makes sense to get the value of the pixel in the output image?
The way this is done for Sobel edge detection is to take these two
values (call them `g_x` and `g_y`, and do the following:

\

![Equation](https://math.now.sh?from=%5Ctext%7Boutput%7D%20%3D%20%5Csqrt%7Bg%5C_x%5E2%20%2B%20g%5C_y%5E2%7D)

\

If you're observant, you'll notice that this is exactly the hypotenuse
of the triangle formed by the values for the `x` and `y` directions.
I'll leave out the specifics for why exactly this is, but it should
intuitively make some sense to combine them this way. Of course, we will
also need to additionally make sure that this output is converted to an
integer from `0-255` by rounding down and capping the maximum. Also,
note that taking the square of both values ensures that `output` will
always be a positive number.

 

****Example****

This can be confusing to understand, so let's look at one example. Let's
assume we have an image of `4x4` pixels, each pixel contains a number
between `0-255`. Let's evaluate the `x` and `y` values of the pixel
`(2, 2)`.

 

- First, computing using G~X~:

![xval.jpeg](/courses/192878/files/11667618/preview)

Note that this is a very high value since there **is** a sharp change in
colour in the `X` direction at pixel `(2, 2)`!

 

- Then, computing using G~Y~:

![yval.jpeg](/courses/192878/files/11667616/preview)

Note that this is 0, since we have no change in colour in the `Y`
direction at this pixel.

 

- Finally, combining the two values for pixel `(2, 2)`:

\

![total.jpeg](/courses/192878/files/11667621/preview)

\

Since 400 \> 255, we will simply set the output to the brightest
possible value, and the final colour for the pixel would then be 255
(white).

 

****Download Starter Code:
[ex7.zip](/courses/192878/files/13586720?wrap=1 "ex7.zip")****

Read over the starter code and make sure you understand how we call the
functions and how we are testing your output. When you are testing, keep
in mind that we are working with `512x512` `.pgm` black and white
pictures as this method of edge detection does not handle colours well.

 

****

#### **What to do:**

-   Implement the `convolve()` and `sobel()` functions in the starter
    code. The documentation in the code gives you some implementation
    details on how to handle the edge cases, as well as tests for both
    functions.

 

**What NOT to do:**

-   Change the name of any functions in the starter code
-   Remove the `#ifndef __testing__` and `#endif` lines

 

#### **What to submit:**

You will submit your `ex7.c` program file only. The file name does not
matter. Do not submit `imgUtils.c`.

1617595140 04/04/2021 11:59pm

-   [File Upload](#submit_online_upload_form)
-   [O365 OneDrive](#submit_from_external_tool_form_5716)

Upload a file, or choose a file you've already uploaded.

File:

** Add Another File

[**remove empty attachment](#)

This file type is not allowed. Accepted file types are: c

Click here to find a file you've already uploaded

\

Cancel

Submit Assignment

Description

Long Description

Cancel

Update Criterion

Additional Comments:

Cancel

Update Comments

Additional Comments:

Rating Score

Rating max score to \> pts

Rating Title

Rating Description

Cancel

Update Rating

Rubric
------

[**](/courses/192878/rubrics/%7B%7B%20id%20%7D%7D "Edit Rubric")
[**](https://q.utoronto.ca/search/rubrics?q= "Find Another Rubric")
[**](/courses/192878/rubric_associations/%7B%7B%20rubric_association_id%20%7D%7D "Delete Rubric")

 

 

 

 

 

 

 

[ ](/courses/192878/rubric_associations/%7B%7B%20rubric_association_id%20%7D%7D/assessments/%7B%7B%20assessment_id%20%7D%7D)
[ ](/courses/192878/rubrics/%7B%7B%20rubric_id%20%7D%7D)
[ ](/courses/192878/rubric_associations/%7B%7B%20association_id%20%7D%7D)

Can't change a rubric once you've started using it.
[ ](/courses/192878/rubric_associations/%7B%7B%20association_id%20%7D%7D)

[Find a
Rubric](https://q.utoronto.ca/search/rubrics?q= "Find Existing Rubric")

Title:
[![](https://du11hjcvx0uqb.cloudfront.net/br/dist/images/find-6164443e2a.png)
Find Rubric](https://q.utoronto.ca/search/rubrics?q=)

Title

You've already rated students with this rubric. Any major changes could
affect their assessment results.

Title

Criteria

Ratings

Pts

[**Edit criterion description](#) [**Delete criterion row](#)

** This criterion is linked to a Learning Outcome Description of
criterion

Range

threshold: 5 pts

  ------------------------------------ ------------------------------------
  [**Edit rating](#) [**Delete         [**Edit rating](#) [**Delete
  rating](#)                           rating](#)
  5 to \>0 pts                         0 to \>0 pts
  Full Marks                           No Marks
  blank                                blank\_2
  [**](#)                              
  ------------------------------------ ------------------------------------

This area will be used by the assessor to leave comments related to this
criterion.

pts \

  / 5 pts\

--

[![Additional
Comments](https://du11hjcvx0uqb.cloudfront.net/br/dist/images/rubric_comment-ddae8546ab.png)](# "Additional Comments")

Total Points: 5 out of 5

  ------------------------------------------------------------------------
  I'll write free-form comments when assessing students
  Remove points from rubric
  Don't post Outcomes results to Learning Mastery Gradebook
  Use this rubric for assignment grading
  Hide score total for assessment results
  Cancel
  Create Rubric
  ------------------------------------------------------------------------

Submission
----------

** Submitted!

Mar 29 at 5:46pm

[Submission
Details](/courses/192878/assignments/516126/submissions/385453)

[Download
ex7-1.c](/courses/192878/assignments/516126/submissions/385453?download=13595552)

success

Grade: 4 (4 pts possible)

Graded Anonymously: no

### Comments:

This is the pre-run result. Please see attached file.

[report.txt](/courses/192878/assignments/516126/submissions/385453?comment_id=4370532&download=13711959)

Charles Xu, Apr 3 at 12:27am

d9310b1f-c79e-4da6-9644-b04565a88594
