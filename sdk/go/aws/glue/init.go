// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
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
	case "aws-native:glue:Classifier":
		r = &Classifier{}
	case "aws-native:glue:Connection":
		r = &Connection{}
	case "aws-native:glue:Crawler":
		r = &Crawler{}
	case "aws-native:glue:CustomEntityType":
		r = &CustomEntityType{}
	case "aws-native:glue:DataCatalogEncryptionSettings":
		r = &DataCatalogEncryptionSettings{}
	case "aws-native:glue:DataQualityRuleset":
		r = &DataQualityRuleset{}
	case "aws-native:glue:Database":
		r = &Database{}
	case "aws-native:glue:DevEndpoint":
		r = &DevEndpoint{}
	case "aws-native:glue:Job":
		r = &Job{}
	case "aws-native:glue:MlTransform":
		r = &MlTransform{}
	case "aws-native:glue:Partition":
		r = &Partition{}
	case "aws-native:glue:Registry":
		r = &Registry{}
	case "aws-native:glue:Schema":
		r = &Schema{}
	case "aws-native:glue:SchemaVersion":
		r = &SchemaVersion{}
	case "aws-native:glue:SchemaVersionMetadata":
		r = &SchemaVersionMetadata{}
	case "aws-native:glue:SecurityConfiguration":
		r = &SecurityConfiguration{}
	case "aws-native:glue:Table":
		r = &Table{}
	case "aws-native:glue:TableOptimizer":
		r = &TableOptimizer{}
	case "aws-native:glue:Trigger":
		r = &Trigger{}
	case "aws-native:glue:Workflow":
		r = &Workflow{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"glue",
		&module{version},
	)
}
