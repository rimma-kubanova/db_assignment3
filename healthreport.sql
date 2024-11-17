--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Homebrew)
-- Dumped by pg_dump version 14.13 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: country; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.country (
    cname character varying(50) NOT NULL,
    population bigint
);


ALTER TABLE public.country OWNER TO postgres;

--
-- Name: discover; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.discover (
    cname character varying(50) NOT NULL,
    disease_code character varying(50) NOT NULL,
    first_enc_date date
);


ALTER TABLE public.discover OWNER TO postgres;

--
-- Name: disease; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.disease (
    disease_code character varying(50) NOT NULL,
    pathogen character varying(20),
    description character varying(140),
    id integer
);


ALTER TABLE public.disease OWNER TO postgres;

--
-- Name: diseasetype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diseasetype (
    id integer NOT NULL,
    description character varying(140)
);


ALTER TABLE public.diseasetype OWNER TO postgres;

--
-- Name: doctor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.doctor (
    email character varying(60) NOT NULL,
    degree character varying(20)
);


ALTER TABLE public.doctor OWNER TO postgres;

--
-- Name: patientdisease; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patientdisease (
    email character varying(60) NOT NULL,
    disease_code character varying(50) NOT NULL
);


ALTER TABLE public.patientdisease OWNER TO postgres;

--
-- Name: patients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patients (
    email character varying(60) NOT NULL
);


ALTER TABLE public.patients OWNER TO postgres;

--
-- Name: publicservant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publicservant (
    email character varying(60) NOT NULL,
    department character varying(50)
);


ALTER TABLE public.publicservant OWNER TO postgres;

--
-- Name: record; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.record (
    email character varying(60) NOT NULL,
    cname character varying(50) NOT NULL,
    disease_code character varying(50) NOT NULL,
    total_deaths integer,
    total_patients integer
);


ALTER TABLE public.record OWNER TO postgres;

--
-- Name: specialize; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.specialize (
    id integer NOT NULL,
    email character varying(60) NOT NULL
);


ALTER TABLE public.specialize OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    email character varying(60) NOT NULL,
    name character varying(30),
    surname character varying(40),
    salary integer,
    phone character varying(20),
    cname character varying(50)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.country (cname, population) FROM stdin;
USA	331000000
Canada	38000000
UK	67000000
France	65000000
Germany	83000000
Italy	60000000
India	1380000000
China	1440000000
Japan	126000000
Australia	25000000
\.


--
-- Data for Name: discover; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.discover (cname, disease_code, first_enc_date) FROM stdin;
USA	D001	1980-01-01
Canada	D002	2000-01-01
UK	D003	1950-05-05
France	D004	1995-07-10
Germany	D005	1990-08-15
Italy	D006	2010-09-01
India	D007	2014-03-20
China	D008	1965-11-25
Japan	D009	2020-05-18
Australia	D010	2016-07-30
USA	D011	1882-01-01
India	D012	1885-01-01
UK	D013	1887-01-01
France	D014	1873-01-01
Germany	D015	1894-01-01
\.


--
-- Data for Name: disease; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.disease (disease_code, pathogen, description, id) FROM stdin;
D005	Cholera	Bacterial infection that causes severe diarrhea and dehydration	2
D008	Leprosy	Chronic bacterial infection that affects the skin and nerves	2
D009	Candidiasis	Fungal infection caused by yeast-like fungi	3
D015	Bacteria	Tuberculosis	1
D014	Bacteria	Cholera	2
D013	Bacteria	Salmonellosis	3
D012	Bacteria	Leprosy	4
D002	Influenza	COVID-19	1
D010	Zika	COVID-19	1
D001	HIV	COVID-19	1
D004	Malaria	COVID-19	4
D011	Bacteria	COVID-19	5
D003	Tuberculosis	COVID-19	2
D006	Athlete Foot	COVID-19	3
D007	Ebola	COVID-19	1
\.


--
-- Data for Name: diseasetype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.diseasetype (id, description) FROM stdin;
3	Fungal Infection
5	Genetic Disorder
6	Autoimmune Disorder
8	Metabolic Disorder
9	Neurological Disorder
10	Psychiatric Disorder
1	Infectious Diseases
2	Infectious Diseases
7	Virology
4	Virology
\.


--
-- Data for Name: doctor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.doctor (email, degree) FROM stdin;
yuji.itadori@example.com	BS
megumi.fushiguro@example.com	MD
nobara.kugisaki@example.com	PhD
satoru.gojo@example.com	DO
suguru.geto@example.com	MD
ryomen.sukuna@example.com	MBBS
kinji.hakari@example.com	MD
toge.inumaki@example.com	DO
maki.zenin@example.com	PhD
yuta.okkotsu@example.com	MD
\.


--
-- Data for Name: patientdisease; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patientdisease (email, disease_code) FROM stdin;
yuji.itadori@example.com	D001
megumi.fushiguro@example.com	D002
nobara.kugisaki@example.com	D003
satoru.gojo@example.com	D004
suguru.geto@example.com	D005
ryomen.sukuna@example.com	D006
kinji.hakari@example.com	D007
toge.inumaki@example.com	D008
maki.zenin@example.com	D009
yuta.okkotsu@example.com	D010
\.


--
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patients (email) FROM stdin;
yuji.itadori@example.com
megumi.fushiguro@example.com
nobara.kugisaki@example.com
satoru.gojo@example.com
suguru.geto@example.com
ryomen.sukuna@example.com
kinji.hakari@example.com
toge.inumaki@example.com
maki.zenin@example.com
yuta.okkotsu@example.com
\.


--
-- Data for Name: publicservant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.publicservant (email, department) FROM stdin;
megumi.fushiguro@example.com	Finance
satoru.gojo@example.com	Research
suguru.geto@example.com	Education
ryomen.sukuna@example.com	Defense
toge.inumaki@example.com	Health
maki.zenin@example.com	Environment
yuta.okkotsu@example.com	Research
yuji.itadori@example.com	Health
nobara.kugisaki@example.com	Health
kinji.hakari@example.com	Health
\.


--
-- Data for Name: record; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.record (email, cname, disease_code, total_deaths, total_patients) FROM stdin;
yuji.itadori@example.com	Japan	D001	1000	50000
megumi.fushiguro@example.com	Canada	D002	500	20000
nobara.kugisaki@example.com	USA	D003	300	15000
satoru.gojo@example.com	Australia	D004	150	5000
suguru.geto@example.com	France	D005	200	10000
ryomen.sukuna@example.com	France	D006	400	25000
kinji.hakari@example.com	USA	D007	600	45000
toge.inumaki@example.com	UK	D008	120	4000
maki.zenin@example.com	Germany	D009	75	3500
yuta.okkotsu@example.com	Japan	D010	800	12000
\.


--
-- Data for Name: specialize; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.specialize (id, email) FROM stdin;
1	yuji.itadori@example.com
2	yuji.itadori@example.com
3	yuji.itadori@example.com
4	satoru.gojo@example.com
5	satoru.gojo@example.com
6	satoru.gojo@example.com
7	suguru.geto@example.com
8	ryomen.sukuna@example.com
9	kinji.hakari@example.com
10	toge.inumaki@example.com
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (email, name, surname, salary, phone, cname) FROM stdin;
satoru.gojo@example.com	Satoru	Gojo	100000	4445556666	Australia
suguru.geto@example.com	Suguru	Geto	90000	7778889999	Japan
ryomen.sukuna@example.com	Ryomen	Sukuna	150000	8889990000	France
kinji.hakari@example.com	Kinji	Hakari	60000	2223334444	USA
toge.inumaki@example.com	Toge	Inumaki	55000	5556667777	UK
maki.zenin@example.com	Maki	Zenin	57000	3334445555	UK
yuta.okkotsu@example.com	Yuta	Okkotsu	60000	6667778888	Japan
yuji.itadori@example.com	Yujibek	Itadori	50000	1234567890	Japan
megumi.fushiguro@example.com	Megumigul	Fushiguro	52000	0987654321	Canada
nobara.kugisaki@example.com	Nobarabek	Kugisaki	51000	1112223333	USA
\.


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (cname);


--
-- Name: discover discover_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discover
    ADD CONSTRAINT discover_pkey PRIMARY KEY (cname, disease_code);


--
-- Name: disease disease_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disease
    ADD CONSTRAINT disease_pkey PRIMARY KEY (disease_code);


--
-- Name: diseasetype diseasetype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diseasetype
    ADD CONSTRAINT diseasetype_pkey PRIMARY KEY (id);


--
-- Name: doctor doctor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor
    ADD CONSTRAINT doctor_pkey PRIMARY KEY (email);


--
-- Name: patientdisease patientdisease_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patientdisease
    ADD CONSTRAINT patientdisease_pkey PRIMARY KEY (email, disease_code);


--
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (email);


--
-- Name: publicservant publicservant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publicservant
    ADD CONSTRAINT publicservant_pkey PRIMARY KEY (email);


--
-- Name: record record_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_pkey PRIMARY KEY (email, cname, disease_code);


--
-- Name: specialize specialize_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specialize
    ADD CONSTRAINT specialize_pkey PRIMARY KEY (id, email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (email);


--
-- Name: discover discover_cname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discover
    ADD CONSTRAINT discover_cname_fkey FOREIGN KEY (cname) REFERENCES public.country(cname);


--
-- Name: discover discover_disease_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discover
    ADD CONSTRAINT discover_disease_code_fkey FOREIGN KEY (disease_code) REFERENCES public.disease(disease_code);


--
-- Name: disease disease_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.disease
    ADD CONSTRAINT disease_id_fkey FOREIGN KEY (id) REFERENCES public.diseasetype(id);


--
-- Name: doctor doctor_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctor
    ADD CONSTRAINT doctor_email_fkey FOREIGN KEY (email) REFERENCES public.users(email) ON DELETE CASCADE;


--
-- Name: patientdisease patientdisease_disease_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patientdisease
    ADD CONSTRAINT patientdisease_disease_code_fkey FOREIGN KEY (disease_code) REFERENCES public.disease(disease_code);


--
-- Name: patientdisease patientdisease_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patientdisease
    ADD CONSTRAINT patientdisease_email_fkey FOREIGN KEY (email) REFERENCES public.users(email) ON DELETE CASCADE;


--
-- Name: patients patients_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_email_fkey FOREIGN KEY (email) REFERENCES public.users(email) ON DELETE CASCADE;


--
-- Name: publicservant publicservant_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publicservant
    ADD CONSTRAINT publicservant_email_fkey FOREIGN KEY (email) REFERENCES public.users(email) ON DELETE CASCADE;


--
-- Name: record record_cname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_cname_fkey FOREIGN KEY (cname) REFERENCES public.country(cname);


--
-- Name: record record_disease_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_disease_code_fkey FOREIGN KEY (disease_code) REFERENCES public.disease(disease_code);


--
-- Name: record record_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_email_fkey FOREIGN KEY (email) REFERENCES public.publicservant(email) ON DELETE CASCADE;


--
-- Name: specialize specialize_email_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specialize
    ADD CONSTRAINT specialize_email_fkey FOREIGN KEY (email) REFERENCES public.doctor(email) ON DELETE CASCADE;


--
-- Name: specialize specialize_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.specialize
    ADD CONSTRAINT specialize_id_fkey FOREIGN KEY (id) REFERENCES public.diseasetype(id);


--
-- Name: users users_cname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_cname_fkey FOREIGN KEY (cname) REFERENCES public.country(cname);


--
-- PostgreSQL database dump complete
--

