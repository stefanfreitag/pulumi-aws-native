// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appintegrations

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppIntegrations::DataIntegration
type DataIntegration struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the data integration.
	DataIntegrationArn pulumi.StringOutput `pulumi:"dataIntegrationArn"`
	// The data integration description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The configuration for what files should be pulled from the source.
	FileConfiguration DataIntegrationFileConfigurationPtrOutput `pulumi:"fileConfiguration"`
	// The KMS key of the data integration.
	KmsKey pulumi.StringOutput `pulumi:"kmsKey"`
	// The name of the data integration.
	Name pulumi.StringOutput `pulumi:"name"`
	// The configuration for what data should be pulled from the source.
	ObjectConfiguration DataIntegrationObjectConfigurationPtrOutput `pulumi:"objectConfiguration"`
	// The name of the data and how often it should be pulled from the source.
	ScheduleConfig DataIntegrationScheduleConfigPtrOutput `pulumi:"scheduleConfig"`
	// The URI of the data source.
	SourceUri pulumi.StringOutput `pulumi:"sourceUri"`
	// The tags (keys and values) associated with the data integration.
	Tags DataIntegrationTagArrayOutput `pulumi:"tags"`
}

// NewDataIntegration registers a new resource with the given unique name, arguments, and options.
func NewDataIntegration(ctx *pulumi.Context,
	name string, args *DataIntegrationArgs, opts ...pulumi.ResourceOption) (*DataIntegration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KmsKey == nil {
		return nil, errors.New("invalid value for required argument 'KmsKey'")
	}
	if args.SourceUri == nil {
		return nil, errors.New("invalid value for required argument 'SourceUri'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"kmsKey",
		"scheduleConfig",
		"sourceUri",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DataIntegration
	err := ctx.RegisterResource("aws-native:appintegrations:DataIntegration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataIntegration gets an existing DataIntegration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataIntegration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataIntegrationState, opts ...pulumi.ResourceOption) (*DataIntegration, error) {
	var resource DataIntegration
	err := ctx.ReadResource("aws-native:appintegrations:DataIntegration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataIntegration resources.
type dataIntegrationState struct {
}

type DataIntegrationState struct {
}

func (DataIntegrationState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataIntegrationState)(nil)).Elem()
}

type dataIntegrationArgs struct {
	// The data integration description.
	Description *string `pulumi:"description"`
	// The configuration for what files should be pulled from the source.
	FileConfiguration *DataIntegrationFileConfiguration `pulumi:"fileConfiguration"`
	// The KMS key of the data integration.
	KmsKey string `pulumi:"kmsKey"`
	// The name of the data integration.
	Name *string `pulumi:"name"`
	// The configuration for what data should be pulled from the source.
	ObjectConfiguration *DataIntegrationObjectConfiguration `pulumi:"objectConfiguration"`
	// The name of the data and how often it should be pulled from the source.
	ScheduleConfig *DataIntegrationScheduleConfig `pulumi:"scheduleConfig"`
	// The URI of the data source.
	SourceUri string `pulumi:"sourceUri"`
	// The tags (keys and values) associated with the data integration.
	Tags []DataIntegrationTag `pulumi:"tags"`
}

// The set of arguments for constructing a DataIntegration resource.
type DataIntegrationArgs struct {
	// The data integration description.
	Description pulumi.StringPtrInput
	// The configuration for what files should be pulled from the source.
	FileConfiguration DataIntegrationFileConfigurationPtrInput
	// The KMS key of the data integration.
	KmsKey pulumi.StringInput
	// The name of the data integration.
	Name pulumi.StringPtrInput
	// The configuration for what data should be pulled from the source.
	ObjectConfiguration DataIntegrationObjectConfigurationPtrInput
	// The name of the data and how often it should be pulled from the source.
	ScheduleConfig DataIntegrationScheduleConfigPtrInput
	// The URI of the data source.
	SourceUri pulumi.StringInput
	// The tags (keys and values) associated with the data integration.
	Tags DataIntegrationTagArrayInput
}

func (DataIntegrationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataIntegrationArgs)(nil)).Elem()
}

type DataIntegrationInput interface {
	pulumi.Input

	ToDataIntegrationOutput() DataIntegrationOutput
	ToDataIntegrationOutputWithContext(ctx context.Context) DataIntegrationOutput
}

func (*DataIntegration) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegration)(nil)).Elem()
}

func (i *DataIntegration) ToDataIntegrationOutput() DataIntegrationOutput {
	return i.ToDataIntegrationOutputWithContext(context.Background())
}

func (i *DataIntegration) ToDataIntegrationOutputWithContext(ctx context.Context) DataIntegrationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataIntegrationOutput)
}

func (i *DataIntegration) ToOutput(ctx context.Context) pulumix.Output[*DataIntegration] {
	return pulumix.Output[*DataIntegration]{
		OutputState: i.ToDataIntegrationOutputWithContext(ctx).OutputState,
	}
}

type DataIntegrationOutput struct{ *pulumi.OutputState }

func (DataIntegrationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataIntegration)(nil)).Elem()
}

func (o DataIntegrationOutput) ToDataIntegrationOutput() DataIntegrationOutput {
	return o
}

func (o DataIntegrationOutput) ToDataIntegrationOutputWithContext(ctx context.Context) DataIntegrationOutput {
	return o
}

func (o DataIntegrationOutput) ToOutput(ctx context.Context) pulumix.Output[*DataIntegration] {
	return pulumix.Output[*DataIntegration]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the data integration.
func (o DataIntegrationOutput) DataIntegrationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DataIntegration) pulumi.StringOutput { return v.DataIntegrationArn }).(pulumi.StringOutput)
}

// The data integration description.
func (o DataIntegrationOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataIntegration) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The configuration for what files should be pulled from the source.
func (o DataIntegrationOutput) FileConfiguration() DataIntegrationFileConfigurationPtrOutput {
	return o.ApplyT(func(v *DataIntegration) DataIntegrationFileConfigurationPtrOutput { return v.FileConfiguration }).(DataIntegrationFileConfigurationPtrOutput)
}

// The KMS key of the data integration.
func (o DataIntegrationOutput) KmsKey() pulumi.StringOutput {
	return o.ApplyT(func(v *DataIntegration) pulumi.StringOutput { return v.KmsKey }).(pulumi.StringOutput)
}

// The name of the data integration.
func (o DataIntegrationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DataIntegration) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The configuration for what data should be pulled from the source.
func (o DataIntegrationOutput) ObjectConfiguration() DataIntegrationObjectConfigurationPtrOutput {
	return o.ApplyT(func(v *DataIntegration) DataIntegrationObjectConfigurationPtrOutput { return v.ObjectConfiguration }).(DataIntegrationObjectConfigurationPtrOutput)
}

// The name of the data and how often it should be pulled from the source.
func (o DataIntegrationOutput) ScheduleConfig() DataIntegrationScheduleConfigPtrOutput {
	return o.ApplyT(func(v *DataIntegration) DataIntegrationScheduleConfigPtrOutput { return v.ScheduleConfig }).(DataIntegrationScheduleConfigPtrOutput)
}

// The URI of the data source.
func (o DataIntegrationOutput) SourceUri() pulumi.StringOutput {
	return o.ApplyT(func(v *DataIntegration) pulumi.StringOutput { return v.SourceUri }).(pulumi.StringOutput)
}

// The tags (keys and values) associated with the data integration.
func (o DataIntegrationOutput) Tags() DataIntegrationTagArrayOutput {
	return o.ApplyT(func(v *DataIntegration) DataIntegrationTagArrayOutput { return v.Tags }).(DataIntegrationTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataIntegrationInput)(nil)).Elem(), &DataIntegration{})
	pulumi.RegisterOutputType(DataIntegrationOutput{})
}
