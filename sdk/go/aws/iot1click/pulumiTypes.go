// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot1click

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ProjectPlacementTemplate struct {
	DefaultAttributes interface{} `pulumi:"defaultAttributes"`
	DeviceTemplates   interface{} `pulumi:"deviceTemplates"`
}

// ProjectPlacementTemplateInput is an input type that accepts ProjectPlacementTemplateArgs and ProjectPlacementTemplateOutput values.
// You can construct a concrete instance of `ProjectPlacementTemplateInput` via:
//
//	ProjectPlacementTemplateArgs{...}
type ProjectPlacementTemplateInput interface {
	pulumi.Input

	ToProjectPlacementTemplateOutput() ProjectPlacementTemplateOutput
	ToProjectPlacementTemplateOutputWithContext(context.Context) ProjectPlacementTemplateOutput
}

type ProjectPlacementTemplateArgs struct {
	DefaultAttributes pulumi.Input `pulumi:"defaultAttributes"`
	DeviceTemplates   pulumi.Input `pulumi:"deviceTemplates"`
}

func (ProjectPlacementTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProjectPlacementTemplate)(nil)).Elem()
}

func (i ProjectPlacementTemplateArgs) ToProjectPlacementTemplateOutput() ProjectPlacementTemplateOutput {
	return i.ToProjectPlacementTemplateOutputWithContext(context.Background())
}

func (i ProjectPlacementTemplateArgs) ToProjectPlacementTemplateOutputWithContext(ctx context.Context) ProjectPlacementTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectPlacementTemplateOutput)
}

type ProjectPlacementTemplateOutput struct{ *pulumi.OutputState }

func (ProjectPlacementTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProjectPlacementTemplate)(nil)).Elem()
}

func (o ProjectPlacementTemplateOutput) ToProjectPlacementTemplateOutput() ProjectPlacementTemplateOutput {
	return o
}

func (o ProjectPlacementTemplateOutput) ToProjectPlacementTemplateOutputWithContext(ctx context.Context) ProjectPlacementTemplateOutput {
	return o
}

func (o ProjectPlacementTemplateOutput) DefaultAttributes() pulumi.AnyOutput {
	return o.ApplyT(func(v ProjectPlacementTemplate) interface{} { return v.DefaultAttributes }).(pulumi.AnyOutput)
}

func (o ProjectPlacementTemplateOutput) DeviceTemplates() pulumi.AnyOutput {
	return o.ApplyT(func(v ProjectPlacementTemplate) interface{} { return v.DeviceTemplates }).(pulumi.AnyOutput)
}

type ProjectPlacementTemplatePtrOutput struct{ *pulumi.OutputState }

func (ProjectPlacementTemplatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ProjectPlacementTemplate)(nil)).Elem()
}

func (o ProjectPlacementTemplatePtrOutput) ToProjectPlacementTemplatePtrOutput() ProjectPlacementTemplatePtrOutput {
	return o
}

func (o ProjectPlacementTemplatePtrOutput) ToProjectPlacementTemplatePtrOutputWithContext(ctx context.Context) ProjectPlacementTemplatePtrOutput {
	return o
}

func (o ProjectPlacementTemplatePtrOutput) Elem() ProjectPlacementTemplateOutput {
	return o.ApplyT(func(v *ProjectPlacementTemplate) ProjectPlacementTemplate {
		if v != nil {
			return *v
		}
		var ret ProjectPlacementTemplate
		return ret
	}).(ProjectPlacementTemplateOutput)
}

func (o ProjectPlacementTemplatePtrOutput) DefaultAttributes() pulumi.AnyOutput {
	return o.ApplyT(func(v *ProjectPlacementTemplate) interface{} {
		if v == nil {
			return nil
		}
		return v.DefaultAttributes
	}).(pulumi.AnyOutput)
}

func (o ProjectPlacementTemplatePtrOutput) DeviceTemplates() pulumi.AnyOutput {
	return o.ApplyT(func(v *ProjectPlacementTemplate) interface{} {
		if v == nil {
			return nil
		}
		return v.DeviceTemplates
	}).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProjectPlacementTemplateInput)(nil)).Elem(), ProjectPlacementTemplateArgs{})
	pulumi.RegisterOutputType(ProjectPlacementTemplateOutput{})
	pulumi.RegisterOutputType(ProjectPlacementTemplatePtrOutput{})
}
