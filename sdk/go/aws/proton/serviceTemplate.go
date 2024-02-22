// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package proton

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::Proton::ServiceTemplate Resource Type
type ServiceTemplate struct {
	pulumi.CustomResourceState

	// <p>The Amazon Resource Name (ARN) of the service template.</p>
	Arn pulumi.StringOutput `pulumi:"arn"`
	// <p>A description of the service template.</p>
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// <p>The name of the service template as displayed in the developer interface.</p>
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// <p>A customer provided encryption key that's used to encrypt data.</p>
	EncryptionKey        pulumi.StringPtrOutput               `pulumi:"encryptionKey"`
	Name                 pulumi.StringPtrOutput               `pulumi:"name"`
	PipelineProvisioning ServiceTemplateProvisioningPtrOutput `pulumi:"pipelineProvisioning"`
	// <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p>
	//          <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
	//         <i>Proton User Guide</i>.</p>
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewServiceTemplate registers a new resource with the given unique name, arguments, and options.
func NewServiceTemplate(ctx *pulumi.Context,
	name string, args *ServiceTemplateArgs, opts ...pulumi.ResourceOption) (*ServiceTemplate, error) {
	if args == nil {
		args = &ServiceTemplateArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"encryptionKey",
		"name",
		"pipelineProvisioning",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServiceTemplate
	err := ctx.RegisterResource("aws-native:proton:ServiceTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceTemplate gets an existing ServiceTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceTemplateState, opts ...pulumi.ResourceOption) (*ServiceTemplate, error) {
	var resource ServiceTemplate
	err := ctx.ReadResource("aws-native:proton:ServiceTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceTemplate resources.
type serviceTemplateState struct {
}

type ServiceTemplateState struct {
}

func (ServiceTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceTemplateState)(nil)).Elem()
}

type serviceTemplateArgs struct {
	// <p>A description of the service template.</p>
	Description *string `pulumi:"description"`
	// <p>The name of the service template as displayed in the developer interface.</p>
	DisplayName *string `pulumi:"displayName"`
	// <p>A customer provided encryption key that's used to encrypt data.</p>
	EncryptionKey        *string                      `pulumi:"encryptionKey"`
	Name                 *string                      `pulumi:"name"`
	PipelineProvisioning *ServiceTemplateProvisioning `pulumi:"pipelineProvisioning"`
	// <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p>
	//          <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
	//         <i>Proton User Guide</i>.</p>
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a ServiceTemplate resource.
type ServiceTemplateArgs struct {
	// <p>A description of the service template.</p>
	Description pulumi.StringPtrInput
	// <p>The name of the service template as displayed in the developer interface.</p>
	DisplayName pulumi.StringPtrInput
	// <p>A customer provided encryption key that's used to encrypt data.</p>
	EncryptionKey        pulumi.StringPtrInput
	Name                 pulumi.StringPtrInput
	PipelineProvisioning ServiceTemplateProvisioningPtrInput
	// <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p>
	//          <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
	//         <i>Proton User Guide</i>.</p>
	Tags aws.TagArrayInput
}

func (ServiceTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceTemplateArgs)(nil)).Elem()
}

type ServiceTemplateInput interface {
	pulumi.Input

	ToServiceTemplateOutput() ServiceTemplateOutput
	ToServiceTemplateOutputWithContext(ctx context.Context) ServiceTemplateOutput
}

func (*ServiceTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceTemplate)(nil)).Elem()
}

func (i *ServiceTemplate) ToServiceTemplateOutput() ServiceTemplateOutput {
	return i.ToServiceTemplateOutputWithContext(context.Background())
}

func (i *ServiceTemplate) ToServiceTemplateOutputWithContext(ctx context.Context) ServiceTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceTemplateOutput)
}

type ServiceTemplateOutput struct{ *pulumi.OutputState }

func (ServiceTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceTemplate)(nil)).Elem()
}

func (o ServiceTemplateOutput) ToServiceTemplateOutput() ServiceTemplateOutput {
	return o
}

func (o ServiceTemplateOutput) ToServiceTemplateOutputWithContext(ctx context.Context) ServiceTemplateOutput {
	return o
}

// <p>The Amazon Resource Name (ARN) of the service template.</p>
func (o ServiceTemplateOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceTemplate) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// <p>A description of the service template.</p>
func (o ServiceTemplateOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceTemplate) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// <p>The name of the service template as displayed in the developer interface.</p>
func (o ServiceTemplateOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceTemplate) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// <p>A customer provided encryption key that's used to encrypt data.</p>
func (o ServiceTemplateOutput) EncryptionKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceTemplate) pulumi.StringPtrOutput { return v.EncryptionKey }).(pulumi.StringPtrOutput)
}

func (o ServiceTemplateOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceTemplate) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o ServiceTemplateOutput) PipelineProvisioning() ServiceTemplateProvisioningPtrOutput {
	return o.ApplyT(func(v *ServiceTemplate) ServiceTemplateProvisioningPtrOutput { return v.PipelineProvisioning }).(ServiceTemplateProvisioningPtrOutput)
}

// <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p>
//
//	 <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the
//	<i>Proton User Guide</i>.</p>
func (o ServiceTemplateOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *ServiceTemplate) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceTemplateInput)(nil)).Elem(), &ServiceTemplate{})
	pulumi.RegisterOutputType(ServiceTemplateOutput{})
}
