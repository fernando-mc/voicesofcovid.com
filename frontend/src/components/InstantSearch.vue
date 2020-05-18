<template>
  <ais-instant-search :search-client="searchClient" index-name="voicesofcovid">
    <ais-search-box />
    <ais-hits>
            <div slot="item" slot-scope="{ item }" class="card">
                <div class="content">
                <div class="header">
                    {{ item.name }} | {{ item.job }}
                </div>
                <div class="description">
                    {{ item.description }}
                </div>
                </div>
                <vue-plyr>
                    <audio>
                        <source :src="item.url" type="audio/mp3"/>
                    </audio>
                </vue-plyr>
                <div class="extra content">
                </div>
            </div>
    </ais-hits>
  </ais-instant-search>
</template>

<script>
import algoliasearch from 'algoliasearch/lite';
import 'instantsearch.css/themes/algolia-min.css';

export default {
  name: 'InstantSearch',
  data () {
    return {
      searchClient: algoliasearch(
        '6FDCZS3XGK',
        '7b307c7784194140313487457fd1dcf5'
      ),
    };
  },
};
</script>

<style>
body {
  font-family: sans-serif;
  padding: 1em;
}

.ais-SearchBox {
  margin-bottom: 10px;
}

.ais-Hits-item {
    max-width: 100%;
    position: relative;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    width: 290px;
    min-height: 0;
    padding: 0;
    border-radius: .28571429rem;
    box-shadow: 0 1px 3px 0 #d4d4d5,0 0 0 1px #d4d4d5;
    transition: box-shadow .1s ease,transform .1s ease,-webkit-box-shadow .1s ease,-webkit-transform .1s ease;
    word-wrap: break-word;
    display: flex;
    /* margin: .875em, 0; */
    float: none;
}
.ais-Hits-item {
    font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
    line-height: 1.4285em;
    color: rgba(0,0,0,.87);
    -webkit-box-direction: normal;
    box-sizing: inherit;
    border-radius: .28571429rem .28571429rem 0 0!important;
    border-top: none!important;
    -webkit-box-flex: 1;
    flex-grow: 1;
    border: none;
    background: 0 0;
    box-shadow: none;
    font-size: 1em;
}

.header {
    -webkit-box-direction: normal;
    box-sizing: inherit;
    display: block;
    font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
    color: rgba(0,0,0,.85);
    font-weight: 700;
    font-size: 1.28571429em;
    margin-top: -.21425em;
    line-height: 1.28571429em;
}

.card {
    font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
    line-height: 1.4285em;
    color: rgba(0,0,0,.87);
    box-sizing: inherit;
    max-width: 100%;
    position: relative;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    flex-direction: column;
    width: 290px;
    min-height: 0;
    background: #fff;
    padding: 0;
    border: none;
    border-radius: .28571429rem;
    box-shadow: 0 1px 3px 0 #d4d4d5,0 0 0 1px #d4d4d5;
    transition: box-shadow .1s ease,transform .1s ease,-webkit-box-shadow .1s ease,-webkit-transform .1s ease;
    word-wrap: break-word;
    display: flex;
    margin-left: .5em;
    float: none;
    font-size: 1em;
}

.content{
    font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
    line-height: 1.4285em;
    color: rgba(0,0,0,.87);
    -webkit-box-direction: normal;
    box-sizing: inherit;
    border-radius: .28571429rem .28571429rem 0 0!important;
    border-top: none!important;
    -webkit-box-flex: 1;
    flex-grow: 1;
    border: none;
    background: 0 0;
    margin: 0;
    padding: 1em 1em;
    box-shadow: none;
    font-size: 1em;
}

.description {
    font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
    line-height: 1.4285em;
    -webkit-box-direction: normal;
    font-size: 1em;
    box-sizing: inherit;
    clear: both;
    color: rgba(0,0,0,.68);
    margin-top: .5em;
}
</style>