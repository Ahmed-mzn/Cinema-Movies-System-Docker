<template>
    <section id="hero">
        <v-parallax dark src="@/assets/img/about.jpg" height="750">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="center">
                        <v-col cols="12" md="6" xl="8">
                            <h1 class="display-2 font-weight-bold mb-4">About us</h1>
                            <h1 class="font-weight-light">
                                We are a team of the best developer ever <br />
                                adipisicing elit. Maiores porro voluptatibus <br />
                                delectus nam optio harum!
                            </h1>
                        </v-col>
                        <v-col cols="12" md="6" xl="4" class="hidden-sm-and-down"> </v-col>
                    </v-row>
                </v-col>
            </v-row>
            <div class="svg-border-waves text-white">
                <v-img src="@/assets/img/borderWaves.svg" />
            </div>
        </v-parallax>
        <v-container fluid id="features" class="mt-2">
            <v-row align="center" justify="center">
                <v-col cols="10">
                    <v-row align="center" justify="space-around">
                        <v-col cols="12" sm="11">
                            <h1 class="font-weight-light display-1">La ballena Team</h1>
                            <h3 class="font-weight-light mt-3">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste
                                explicabo commodi quisquam asperiores dolore ad enim provident
                                explicabo commodi quisquam asperiores dolore ad enim provident
                                explicabo commodi quisquam asperiores dolore ad enim provident
                                explicabo commodi quisquam asperiores dolore ad enim provident
                                explicabo commodi quisquam asperiores dolore ad enim provident
                                veniam perferendis voluptate, perspiciatis.
                            </h3>
                            <h3 class="font-weight-light mt-3">
                                Lorem ipsum dolor sit amet consectetur adipisicing.
                            </h3>
                            <!-- <h3 class="font-weight-light mt-3">
                                Téléphone: +xx (xx) xxxxx-xxxx
                            </h3>
                            <h3 class="font-weight-light">
                                Email: email@email.com
                            </h3> -->
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
        <br><br>
        <div class="svg-border-waves">
            <img src="~@/assets/img/wave2.svg" />
        </div>
    </section>
</template>

<script>
export default {
    data() {
        return {};
    },
    watch: {
        dialog(value) {
            if (!value) {
                this.pause();
            }
        },
    },
    methods: {},
};
</script>
