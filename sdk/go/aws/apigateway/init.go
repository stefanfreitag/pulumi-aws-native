// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "aws-native:apigateway:Account":
		r = &Account{}
	case "aws-native:apigateway:ApiKey":
		r = &ApiKey{}
	case "aws-native:apigateway:Authorizer":
		r = &Authorizer{}
	case "aws-native:apigateway:BasePathMapping":
		r = &BasePathMapping{}
	case "aws-native:apigateway:ClientCertificate":
		r = &ClientCertificate{}
	case "aws-native:apigateway:Deployment":
		r = &Deployment{}
	case "aws-native:apigateway:DocumentationPart":
		r = &DocumentationPart{}
	case "aws-native:apigateway:DocumentationVersion":
		r = &DocumentationVersion{}
	case "aws-native:apigateway:DomainName":
		r = &DomainName{}
	case "aws-native:apigateway:GatewayResponse":
		r = &GatewayResponse{}
	case "aws-native:apigateway:Method":
		r = &Method{}
	case "aws-native:apigateway:Model":
		r = &Model{}
	case "aws-native:apigateway:RequestValidator":
		r = &RequestValidator{}
	case "aws-native:apigateway:Resource":
		r = &Resource{}
	case "aws-native:apigateway:RestApi":
		r = &RestApi{}
	case "aws-native:apigateway:Stage":
		r = &Stage{}
	case "aws-native:apigateway:UsagePlan":
		r = &UsagePlan{}
	case "aws-native:apigateway:UsagePlanKey":
		r = &UsagePlanKey{}
	case "aws-native:apigateway:VpcLink":
		r = &VpcLink{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := aws.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"apigateway",
		&module{version},
	)
}
