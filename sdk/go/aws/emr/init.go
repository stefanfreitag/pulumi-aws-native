// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package emr

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
	case "aws-native:emr:Cluster":
		r = &Cluster{}
	case "aws-native:emr:InstanceFleetConfig":
		r = &InstanceFleetConfig{}
	case "aws-native:emr:InstanceGroupConfig":
		r = &InstanceGroupConfig{}
	case "aws-native:emr:SecurityConfiguration":
		r = &SecurityConfiguration{}
	case "aws-native:emr:Step":
		r = &Step{}
	case "aws-native:emr:Studio":
		r = &Studio{}
	case "aws-native:emr:StudioSessionMapping":
		r = &StudioSessionMapping{}
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
		"emr",
		&module{version},
	)
}
