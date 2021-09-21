// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

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
	case "aws-native:apigatewayv2:Api":
		r = &Api{}
	case "aws-native:apigatewayv2:ApiGatewayManagedOverrides":
		r = &ApiGatewayManagedOverrides{}
	case "aws-native:apigatewayv2:ApiMapping":
		r = &ApiMapping{}
	case "aws-native:apigatewayv2:Authorizer":
		r = &Authorizer{}
	case "aws-native:apigatewayv2:Deployment":
		r = &Deployment{}
	case "aws-native:apigatewayv2:DomainName":
		r = &DomainName{}
	case "aws-native:apigatewayv2:Integration":
		r = &Integration{}
	case "aws-native:apigatewayv2:IntegrationResponse":
		r = &IntegrationResponse{}
	case "aws-native:apigatewayv2:Model":
		r = &Model{}
	case "aws-native:apigatewayv2:Route":
		r = &Route{}
	case "aws-native:apigatewayv2:RouteResponse":
		r = &RouteResponse{}
	case "aws-native:apigatewayv2:Stage":
		r = &Stage{}
	case "aws-native:apigatewayv2:VpcLink":
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
		fmt.Printf("failed to determine package version. defaulting to v1: %v\n", err)
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"apigatewayv2",
		&module{version},
	)
}
