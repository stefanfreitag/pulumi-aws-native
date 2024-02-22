// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package opsworks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::OpsWorks::Layer
func LookupLayer(ctx *pulumi.Context, args *LookupLayerArgs, opts ...pulumi.InvokeOption) (*LookupLayerResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLayerResult
	err := ctx.Invoke("aws-native:opsworks:getLayer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLayerArgs struct {
	Id string `pulumi:"id"`
}

type LookupLayerResult struct {
	Attributes               map[string]string `pulumi:"attributes"`
	AutoAssignElasticIps     *bool             `pulumi:"autoAssignElasticIps"`
	AutoAssignPublicIps      *bool             `pulumi:"autoAssignPublicIps"`
	CustomInstanceProfileArn *string           `pulumi:"customInstanceProfileArn"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpsWorks::Layer` for more information about the expected schema for this property.
	CustomJson                  interface{}                       `pulumi:"customJson"`
	CustomRecipes               *LayerRecipes                     `pulumi:"customRecipes"`
	CustomSecurityGroupIds      []string                          `pulumi:"customSecurityGroupIds"`
	EnableAutoHealing           *bool                             `pulumi:"enableAutoHealing"`
	Id                          *string                           `pulumi:"id"`
	InstallUpdatesOnBoot        *bool                             `pulumi:"installUpdatesOnBoot"`
	LifecycleEventConfiguration *LayerLifecycleEventConfiguration `pulumi:"lifecycleEventConfiguration"`
	LoadBasedAutoScaling        *LayerLoadBasedAutoScaling        `pulumi:"loadBasedAutoScaling"`
	Name                        *string                           `pulumi:"name"`
	Packages                    []string                          `pulumi:"packages"`
	Shortname                   *string                           `pulumi:"shortname"`
	Tags                        []aws.Tag                         `pulumi:"tags"`
	UseEbsOptimizedInstances    *bool                             `pulumi:"useEbsOptimizedInstances"`
	VolumeConfigurations        []LayerVolumeConfiguration        `pulumi:"volumeConfigurations"`
}

func LookupLayerOutput(ctx *pulumi.Context, args LookupLayerOutputArgs, opts ...pulumi.InvokeOption) LookupLayerResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLayerResult, error) {
			args := v.(LookupLayerArgs)
			r, err := LookupLayer(ctx, &args, opts...)
			var s LookupLayerResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLayerResultOutput)
}

type LookupLayerOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupLayerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLayerArgs)(nil)).Elem()
}

type LookupLayerResultOutput struct{ *pulumi.OutputState }

func (LookupLayerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLayerResult)(nil)).Elem()
}

func (o LookupLayerResultOutput) ToLookupLayerResultOutput() LookupLayerResultOutput {
	return o
}

func (o LookupLayerResultOutput) ToLookupLayerResultOutputWithContext(ctx context.Context) LookupLayerResultOutput {
	return o
}

func (o LookupLayerResultOutput) Attributes() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupLayerResult) map[string]string { return v.Attributes }).(pulumi.StringMapOutput)
}

func (o LookupLayerResultOutput) AutoAssignElasticIps() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *bool { return v.AutoAssignElasticIps }).(pulumi.BoolPtrOutput)
}

func (o LookupLayerResultOutput) AutoAssignPublicIps() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *bool { return v.AutoAssignPublicIps }).(pulumi.BoolPtrOutput)
}

func (o LookupLayerResultOutput) CustomInstanceProfileArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *string { return v.CustomInstanceProfileArn }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpsWorks::Layer` for more information about the expected schema for this property.
func (o LookupLayerResultOutput) CustomJson() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupLayerResult) interface{} { return v.CustomJson }).(pulumi.AnyOutput)
}

func (o LookupLayerResultOutput) CustomRecipes() LayerRecipesPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *LayerRecipes { return v.CustomRecipes }).(LayerRecipesPtrOutput)
}

func (o LookupLayerResultOutput) CustomSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLayerResult) []string { return v.CustomSecurityGroupIds }).(pulumi.StringArrayOutput)
}

func (o LookupLayerResultOutput) EnableAutoHealing() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *bool { return v.EnableAutoHealing }).(pulumi.BoolPtrOutput)
}

func (o LookupLayerResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupLayerResultOutput) InstallUpdatesOnBoot() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *bool { return v.InstallUpdatesOnBoot }).(pulumi.BoolPtrOutput)
}

func (o LookupLayerResultOutput) LifecycleEventConfiguration() LayerLifecycleEventConfigurationPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *LayerLifecycleEventConfiguration { return v.LifecycleEventConfiguration }).(LayerLifecycleEventConfigurationPtrOutput)
}

func (o LookupLayerResultOutput) LoadBasedAutoScaling() LayerLoadBasedAutoScalingPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *LayerLoadBasedAutoScaling { return v.LoadBasedAutoScaling }).(LayerLoadBasedAutoScalingPtrOutput)
}

func (o LookupLayerResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupLayerResultOutput) Packages() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupLayerResult) []string { return v.Packages }).(pulumi.StringArrayOutput)
}

func (o LookupLayerResultOutput) Shortname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *string { return v.Shortname }).(pulumi.StringPtrOutput)
}

func (o LookupLayerResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupLayerResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func (o LookupLayerResultOutput) UseEbsOptimizedInstances() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupLayerResult) *bool { return v.UseEbsOptimizedInstances }).(pulumi.BoolPtrOutput)
}

func (o LookupLayerResultOutput) VolumeConfigurations() LayerVolumeConfigurationArrayOutput {
	return o.ApplyT(func(v LookupLayerResult) []LayerVolumeConfiguration { return v.VolumeConfigurations }).(LayerVolumeConfigurationArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLayerResultOutput{})
}
