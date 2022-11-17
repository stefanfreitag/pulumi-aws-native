// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

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
	case "aws-native:ses:ConfigurationSet":
		r = &ConfigurationSet{}
	case "aws-native:ses:ConfigurationSetEventDestination":
		r = &ConfigurationSetEventDestination{}
	case "aws-native:ses:ContactList":
		r = &ContactList{}
	case "aws-native:ses:DedicatedIpPool":
		r = &DedicatedIpPool{}
	case "aws-native:ses:EmailIdentity":
		r = &EmailIdentity{}
	case "aws-native:ses:ReceiptFilter":
		r = &ReceiptFilter{}
	case "aws-native:ses:ReceiptRule":
		r = &ReceiptRule{}
	case "aws-native:ses:ReceiptRuleSet":
		r = &ReceiptRuleSet{}
	case "aws-native:ses:Template":
		r = &Template{}
	case "aws-native:ses:VdmAttributes":
		r = &VdmAttributes{}
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
		"ses",
		&module{version},
	)
}
