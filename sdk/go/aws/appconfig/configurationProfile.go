// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppConfig::ConfigurationProfile
//
// Deprecated: ConfigurationProfile is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ConfigurationProfile struct {
	pulumi.CustomResourceState

	ApplicationId    pulumi.StringOutput                       `pulumi:"applicationId"`
	Description      pulumi.StringPtrOutput                    `pulumi:"description"`
	LocationUri      pulumi.StringOutput                       `pulumi:"locationUri"`
	Name             pulumi.StringOutput                       `pulumi:"name"`
	RetrievalRoleArn pulumi.StringPtrOutput                    `pulumi:"retrievalRoleArn"`
	Tags             ConfigurationProfileTagsArrayOutput       `pulumi:"tags"`
	Type             pulumi.StringPtrOutput                    `pulumi:"type"`
	Validators       ConfigurationProfileValidatorsArrayOutput `pulumi:"validators"`
}

// NewConfigurationProfile registers a new resource with the given unique name, arguments, and options.
func NewConfigurationProfile(ctx *pulumi.Context,
	name string, args *ConfigurationProfileArgs, opts ...pulumi.ResourceOption) (*ConfigurationProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	if args.LocationUri == nil {
		return nil, errors.New("invalid value for required argument 'LocationUri'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"applicationId",
		"locationUri",
		"type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ConfigurationProfile
	err := ctx.RegisterResource("aws-native:appconfig:ConfigurationProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationProfile gets an existing ConfigurationProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationProfileState, opts ...pulumi.ResourceOption) (*ConfigurationProfile, error) {
	var resource ConfigurationProfile
	err := ctx.ReadResource("aws-native:appconfig:ConfigurationProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationProfile resources.
type configurationProfileState struct {
}

type ConfigurationProfileState struct {
}

func (ConfigurationProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationProfileState)(nil)).Elem()
}

type configurationProfileArgs struct {
	ApplicationId    string                           `pulumi:"applicationId"`
	Description      *string                          `pulumi:"description"`
	LocationUri      string                           `pulumi:"locationUri"`
	Name             *string                          `pulumi:"name"`
	RetrievalRoleArn *string                          `pulumi:"retrievalRoleArn"`
	Tags             []ConfigurationProfileTags       `pulumi:"tags"`
	Type             *string                          `pulumi:"type"`
	Validators       []ConfigurationProfileValidators `pulumi:"validators"`
}

// The set of arguments for constructing a ConfigurationProfile resource.
type ConfigurationProfileArgs struct {
	ApplicationId    pulumi.StringInput
	Description      pulumi.StringPtrInput
	LocationUri      pulumi.StringInput
	Name             pulumi.StringPtrInput
	RetrievalRoleArn pulumi.StringPtrInput
	Tags             ConfigurationProfileTagsArrayInput
	Type             pulumi.StringPtrInput
	Validators       ConfigurationProfileValidatorsArrayInput
}

func (ConfigurationProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationProfileArgs)(nil)).Elem()
}

type ConfigurationProfileInput interface {
	pulumi.Input

	ToConfigurationProfileOutput() ConfigurationProfileOutput
	ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput
}

func (*ConfigurationProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationProfile)(nil)).Elem()
}

func (i *ConfigurationProfile) ToConfigurationProfileOutput() ConfigurationProfileOutput {
	return i.ToConfigurationProfileOutputWithContext(context.Background())
}

func (i *ConfigurationProfile) ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationProfileOutput)
}

func (i *ConfigurationProfile) ToOutput(ctx context.Context) pulumix.Output[*ConfigurationProfile] {
	return pulumix.Output[*ConfigurationProfile]{
		OutputState: i.ToConfigurationProfileOutputWithContext(ctx).OutputState,
	}
}

type ConfigurationProfileOutput struct{ *pulumi.OutputState }

func (ConfigurationProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationProfile)(nil)).Elem()
}

func (o ConfigurationProfileOutput) ToConfigurationProfileOutput() ConfigurationProfileOutput {
	return o
}

func (o ConfigurationProfileOutput) ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput {
	return o
}

func (o ConfigurationProfileOutput) ToOutput(ctx context.Context) pulumix.Output[*ConfigurationProfile] {
	return pulumix.Output[*ConfigurationProfile]{
		OutputState: o.OutputState,
	}
}

func (o ConfigurationProfileOutput) ApplicationId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringOutput { return v.ApplicationId }).(pulumi.StringOutput)
}

func (o ConfigurationProfileOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o ConfigurationProfileOutput) LocationUri() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringOutput { return v.LocationUri }).(pulumi.StringOutput)
}

func (o ConfigurationProfileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ConfigurationProfileOutput) RetrievalRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringPtrOutput { return v.RetrievalRoleArn }).(pulumi.StringPtrOutput)
}

func (o ConfigurationProfileOutput) Tags() ConfigurationProfileTagsArrayOutput {
	return o.ApplyT(func(v *ConfigurationProfile) ConfigurationProfileTagsArrayOutput { return v.Tags }).(ConfigurationProfileTagsArrayOutput)
}

func (o ConfigurationProfileOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConfigurationProfile) pulumi.StringPtrOutput { return v.Type }).(pulumi.StringPtrOutput)
}

func (o ConfigurationProfileOutput) Validators() ConfigurationProfileValidatorsArrayOutput {
	return o.ApplyT(func(v *ConfigurationProfile) ConfigurationProfileValidatorsArrayOutput { return v.Validators }).(ConfigurationProfileValidatorsArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationProfileInput)(nil)).Elem(), &ConfigurationProfile{})
	pulumi.RegisterOutputType(ConfigurationProfileOutput{})
}
