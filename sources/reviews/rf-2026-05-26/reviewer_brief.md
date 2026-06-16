# Word Sense Review — Annotator Brief

## What this is

You are reviewing 363 English sentences. In each one, a single target word is marked. Your job is to
decide, from the WordNet sense inventory shown to you, **which sense the word carries in that
sentence**.

## What the output is used for

Your verdicts feed an automated **word-sense disambiguation (WSD) evaluation pipeline**. The end
consumer is a language-technology system that maps each word occurrence to one sense, so it can be
scored against your judgement.

This matters for one decision you will make repeatedly: **the granularity you work at.** You are
*not* writing a learner's dictionary, where showing someone two near-identical definitions would be
unhelpful. You are identifying, as precisely as the inventory allows, which sense node the author's
meaning belongs under. When two senses are close, that is not a reason to give up and pick both —
see the rules below.

## The core rule: one sense by default

**For each item, select the single sense that best fits the meaning in context.**

Treat the sentence as written by a competent author who had one meaning in mind. Your task is to
recover that meaning and match it to the closest WordNet sense. In the large majority of items, one
sense is clearly the best fit even when other senses are loosely related.

If two senses both seem to fit and you can reason your way to the better one — pick that one and
record lower confidence (see Confidence below). Do **not** select both merely because both are
plausible in isolation.

## When to select multiple senses

Select more than one sense **only** in this specific situation:

> The sentence itself is genuinely ambiguous — a competent reader cannot determine which of two (or
> more) distinct meanings the author intended — **and** each of those meanings is fully supported by
> the context.

This is rare. It is for true ambiguity in the *text*, not for closeness in the *inventory*. If the
senses are close but the author clearly meant one thing, that is a single-sense pick with low
confidence, not a multi-sense pick.

When you do select multiple senses, **add a comment** stating why the sentence is irreducibly
ambiguous.

## The three "cannot answer" flags

If you cannot pick a sense, the reason matters. Use the correct flag — do not collapse all three
into one. Each requires a free-text note.

* **`no_sense_applies`** — The WordNet inventory is complete enough, but none of its senses matches
  this usage. The meaning is clear; the inventory simply lacks it. Note what the correct sense
  *would* be.
* **`inventory_inadequate`** — WordNet *has* roughly the right area but cannot express the
  distinction needed here: e.g. the word is genuinely used in a different part of speech than any
  listed sense allows (see the note on noun adjuncts under Worked examples — attributive noun use is
  *not* such a case), the definitions are too obscure or ambiguous to choose between, or the word is
  part of a phrasal verb that WordNet does not list as a separate unit. Note the specific
  inadequacy.
* **`input_defective`** — The problem is the source sentence, not the senses. The text is
  ungrammatical, appears machine-translated or written by a non-native speaker, is missing context
  needed to disambiguate, or is ambiguous for reasons unrelated to word sense. Note what is wrong.

If you can still make a best-effort sense pick despite a flagged problem, do so *and* set the flag
*and* lower your confidence. The flag and the pick are not mutually exclusive.

## Confidence

Rate every verdict:

* **3 — High**: one sense clearly fits; you would be surprised to be wrong.
* **2 — Medium**: you have a best answer but a competing sense is defensible.
* **1 — Low**: you are close to guessing, or you flagged a problem above.

Confidence is as valuable as the verdict itself. A low-confidence verdict is a useful, honest
verdict — it is not a failure.

## Highlighted candidate senses — and what they mean

To save you time scanning long sense lists, the tool highlights up to two **candidate senses** for
each item — senses that other sources (an earlier annotation and an automated system) considered
plausible. Which source proposed which sense is deliberately **not shown**, and you should not try
to guess.

Treat the highlights only as a starting point for your attention. They are **not a hint** that the
answer is one of them:

* The correct sense may be one that is **not** highlighted — consider the full inventory before
  deciding.
* The correct verdict may instead be one of the three "cannot answer" flags — the highlights do not
  discourage that.
* If only one sense is highlighted, that simply means the two sources agreed; it carries no extra
  weight.

Do your own analysis first, then check whether it lands on a highlighted sense or not — either
outcome is equally valid. You will not see the verdicts of other reviewers; please do not seek them
out before finishing.

## Worked examples

These illustrate the rules. They do not reveal any prior verdict.

**Single sense, high confidence.** A sentence uses *court* clearly to mean a judicial body ("the
court ruled against the appeal"). Other senses of *court* exist (a royal court, a tennis court), but
the context settles it. → One sense, confidence 3.

**Close senses, single pick, low confidence.** *Argument* can mean a line of reasoning or a verbal
disagreement, and in some sentences both shades are present. If you judge that the author leaned to
one — pick that one, confidence 1 or 2, and optionally comment. Do **not** select both.

**Genuine textual ambiguity, multiple senses.** A sentence reports that someone *said* words shown
in quotation marks. The marks could mean the words were spoken aloud, or quoted from a written
source — and nothing in the context decides it. Both readings map to different senses of *say*. →
Select both senses, with a comment explaining the ambiguity.

**Noun used attributively — pick the standard noun sense.** A noun placed before another noun to
modify it ("U.S. troops", "water bottle", "government policy") is a *noun adjunct*, not an
adjective. It carries the same meaning as the noun used on its own — *U.S.* in "U.S. troops" is the
same entity as *U.S.* in "I live in the U.S." → Pick the standard noun sense, confidence 3; do
**not** flag a POS mismatch. The only exception is a word that has genuinely lexicalised into a
distinct adjective with a new meaning — e.g. *plastic* meaning "fake" or "superficial" rather than
the material — and only then does a separate sense apply.

**Phrasal verb, `inventory_inadequate`.** The target is *keep*, but the sentence uses the phrasal
verb *keep back* ("she kept back the truth"), which WordNet does not list as a separate lexical
unit. The plain senses of *keep* do not cover it. → `inventory_inadequate`, note the phrasal verb.

**Broken source, `input_defective`.** The sentence is garbled — apparently machine-translated — and
the intended meaning of the target word cannot be recovered with confidence. → `input_defective`,
note that the source text is unreliable; confidence 1.

## Practical notes

* WordNet definitions are sometimes terse or obscurely worded, and WordNet does not mark verbs as
  transitive/intransitive. Read the example sentences WordNet supplies for each sense — they often
  disambiguate better than the definition text.
* Use the full context window (the surrounding sentences), not just the target sentence.
* A comment is always welcome on any verdict, not only the flagged ones. If your reasoning is
  non-obvious, a one-line comment is worth a lot to the analysis.

## Before you submit each item — checklist

1. Did you read the full context window, not just the target sentence?
2. Did you check WordNet's example sentences, not only the definitions?
3. Is this a single best sense (the default), or a true case of textual ambiguity?
4. If you could not pick a sense, did you choose the *correct* one of the three flags and write a
   note?
5. Did you set a confidence rating?
