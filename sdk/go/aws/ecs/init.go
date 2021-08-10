// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

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
	case "aws-native:ECS:CapacityProvider":
		r = &CapacityProvider{}
	case "aws-native:ECS:Cluster":
		r = &Cluster{}
	case "aws-native:ECS:PrimaryTaskSet":
		r = &PrimaryTaskSet{}
	case "aws-native:ECS:Service":
		r = &Service{}
	case "aws-native:ECS:TaskDefinition":
		r = &TaskDefinition{}
	case "aws-native:ECS:TaskSet":
		r = &TaskSet{}
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
		"ECS",
		&module{version},
	)
}
