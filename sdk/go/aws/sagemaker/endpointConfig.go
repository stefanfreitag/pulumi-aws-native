// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::EndpointConfig
//
// Deprecated: EndpointConfig is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type EndpointConfig struct {
	pulumi.CustomResourceState

	AsyncInferenceConfig     EndpointConfigAsyncInferenceConfigPtrOutput `pulumi:"asyncInferenceConfig"`
	DataCaptureConfig        EndpointConfigDataCaptureConfigPtrOutput    `pulumi:"dataCaptureConfig"`
	EndpointConfigName       pulumi.StringPtrOutput                      `pulumi:"endpointConfigName"`
	ExplainerConfig          EndpointConfigExplainerConfigPtrOutput      `pulumi:"explainerConfig"`
	KmsKeyId                 pulumi.StringPtrOutput                      `pulumi:"kmsKeyId"`
	ProductionVariants       EndpointConfigProductionVariantArrayOutput  `pulumi:"productionVariants"`
	ShadowProductionVariants EndpointConfigProductionVariantArrayOutput  `pulumi:"shadowProductionVariants"`
	Tags                     EndpointConfigTagArrayOutput                `pulumi:"tags"`
}

// NewEndpointConfig registers a new resource with the given unique name, arguments, and options.
func NewEndpointConfig(ctx *pulumi.Context,
	name string, args *EndpointConfigArgs, opts ...pulumi.ResourceOption) (*EndpointConfig, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProductionVariants == nil {
		return nil, errors.New("invalid value for required argument 'ProductionVariants'")
	}
	var resource EndpointConfig
	err := ctx.RegisterResource("aws-native:sagemaker:EndpointConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpointConfig gets an existing EndpointConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpointConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointConfigState, opts ...pulumi.ResourceOption) (*EndpointConfig, error) {
	var resource EndpointConfig
	err := ctx.ReadResource("aws-native:sagemaker:EndpointConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EndpointConfig resources.
type endpointConfigState struct {
}

type EndpointConfigState struct {
}

func (EndpointConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointConfigState)(nil)).Elem()
}

type endpointConfigArgs struct {
	AsyncInferenceConfig     *EndpointConfigAsyncInferenceConfig `pulumi:"asyncInferenceConfig"`
	DataCaptureConfig        *EndpointConfigDataCaptureConfig    `pulumi:"dataCaptureConfig"`
	EndpointConfigName       *string                             `pulumi:"endpointConfigName"`
	ExplainerConfig          *EndpointConfigExplainerConfig      `pulumi:"explainerConfig"`
	KmsKeyId                 *string                             `pulumi:"kmsKeyId"`
	ProductionVariants       []EndpointConfigProductionVariant   `pulumi:"productionVariants"`
	ShadowProductionVariants []EndpointConfigProductionVariant   `pulumi:"shadowProductionVariants"`
	Tags                     []EndpointConfigTag                 `pulumi:"tags"`
}

// The set of arguments for constructing a EndpointConfig resource.
type EndpointConfigArgs struct {
	AsyncInferenceConfig     EndpointConfigAsyncInferenceConfigPtrInput
	DataCaptureConfig        EndpointConfigDataCaptureConfigPtrInput
	EndpointConfigName       pulumi.StringPtrInput
	ExplainerConfig          EndpointConfigExplainerConfigPtrInput
	KmsKeyId                 pulumi.StringPtrInput
	ProductionVariants       EndpointConfigProductionVariantArrayInput
	ShadowProductionVariants EndpointConfigProductionVariantArrayInput
	Tags                     EndpointConfigTagArrayInput
}

func (EndpointConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointConfigArgs)(nil)).Elem()
}

type EndpointConfigInput interface {
	pulumi.Input

	ToEndpointConfigOutput() EndpointConfigOutput
	ToEndpointConfigOutputWithContext(ctx context.Context) EndpointConfigOutput
}

func (*EndpointConfig) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointConfig)(nil)).Elem()
}

func (i *EndpointConfig) ToEndpointConfigOutput() EndpointConfigOutput {
	return i.ToEndpointConfigOutputWithContext(context.Background())
}

func (i *EndpointConfig) ToEndpointConfigOutputWithContext(ctx context.Context) EndpointConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointConfigOutput)
}

type EndpointConfigOutput struct{ *pulumi.OutputState }

func (EndpointConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointConfig)(nil)).Elem()
}

func (o EndpointConfigOutput) ToEndpointConfigOutput() EndpointConfigOutput {
	return o
}

func (o EndpointConfigOutput) ToEndpointConfigOutputWithContext(ctx context.Context) EndpointConfigOutput {
	return o
}

func (o EndpointConfigOutput) AsyncInferenceConfig() EndpointConfigAsyncInferenceConfigPtrOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigAsyncInferenceConfigPtrOutput { return v.AsyncInferenceConfig }).(EndpointConfigAsyncInferenceConfigPtrOutput)
}

func (o EndpointConfigOutput) DataCaptureConfig() EndpointConfigDataCaptureConfigPtrOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigDataCaptureConfigPtrOutput { return v.DataCaptureConfig }).(EndpointConfigDataCaptureConfigPtrOutput)
}

func (o EndpointConfigOutput) EndpointConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EndpointConfig) pulumi.StringPtrOutput { return v.EndpointConfigName }).(pulumi.StringPtrOutput)
}

func (o EndpointConfigOutput) ExplainerConfig() EndpointConfigExplainerConfigPtrOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigExplainerConfigPtrOutput { return v.ExplainerConfig }).(EndpointConfigExplainerConfigPtrOutput)
}

func (o EndpointConfigOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EndpointConfig) pulumi.StringPtrOutput { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o EndpointConfigOutput) ProductionVariants() EndpointConfigProductionVariantArrayOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigProductionVariantArrayOutput { return v.ProductionVariants }).(EndpointConfigProductionVariantArrayOutput)
}

func (o EndpointConfigOutput) ShadowProductionVariants() EndpointConfigProductionVariantArrayOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigProductionVariantArrayOutput { return v.ShadowProductionVariants }).(EndpointConfigProductionVariantArrayOutput)
}

func (o EndpointConfigOutput) Tags() EndpointConfigTagArrayOutput {
	return o.ApplyT(func(v *EndpointConfig) EndpointConfigTagArrayOutput { return v.Tags }).(EndpointConfigTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointConfigInput)(nil)).Elem(), &EndpointConfig{})
	pulumi.RegisterOutputType(EndpointConfigOutput{})
}
