// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

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
	case "aws-native:iot:AccountAuditConfiguration":
		r = &AccountAuditConfiguration{}
	case "aws-native:iot:Authorizer":
		r = &Authorizer{}
	case "aws-native:iot:Certificate":
		r = &Certificate{}
	case "aws-native:iot:CustomMetric":
		r = &CustomMetric{}
	case "aws-native:iot:Dimension":
		r = &Dimension{}
	case "aws-native:iot:DomainConfiguration":
		r = &DomainConfiguration{}
	case "aws-native:iot:FleetMetric":
		r = &FleetMetric{}
	case "aws-native:iot:JobTemplate":
		r = &JobTemplate{}
	case "aws-native:iot:Logging":
		r = &Logging{}
	case "aws-native:iot:MitigationAction":
		r = &MitigationAction{}
	case "aws-native:iot:Policy":
		r = &Policy{}
	case "aws-native:iot:PolicyPrincipalAttachment":
		r = &PolicyPrincipalAttachment{}
	case "aws-native:iot:ProvisioningTemplate":
		r = &ProvisioningTemplate{}
	case "aws-native:iot:ResourceSpecificLogging":
		r = &ResourceSpecificLogging{}
	case "aws-native:iot:ScheduledAudit":
		r = &ScheduledAudit{}
	case "aws-native:iot:SecurityProfile":
		r = &SecurityProfile{}
	case "aws-native:iot:Thing":
		r = &Thing{}
	case "aws-native:iot:ThingPrincipalAttachment":
		r = &ThingPrincipalAttachment{}
	case "aws-native:iot:TopicRule":
		r = &TopicRule{}
	case "aws-native:iot:TopicRuleDestination":
		r = &TopicRuleDestination{}
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
		"iot",
		&module{version},
	)
}
