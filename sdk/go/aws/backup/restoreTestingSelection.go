// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Backup::RestoreTestingSelection
type RestoreTestingSelection struct {
	pulumi.CustomResourceState

	IamRoleArn                  pulumi.StringOutput                                         `pulumi:"iamRoleArn"`
	ProtectedResourceArns       pulumi.StringArrayOutput                                    `pulumi:"protectedResourceArns"`
	ProtectedResourceConditions RestoreTestingSelectionProtectedResourceConditionsPtrOutput `pulumi:"protectedResourceConditions"`
	ProtectedResourceType       pulumi.StringOutput                                         `pulumi:"protectedResourceType"`
	RestoreMetadataOverrides    RestoreTestingSelectionSensitiveStringMapPtrOutput          `pulumi:"restoreMetadataOverrides"`
	RestoreTestingPlanName      pulumi.StringOutput                                         `pulumi:"restoreTestingPlanName"`
	RestoreTestingSelectionName pulumi.StringOutput                                         `pulumi:"restoreTestingSelectionName"`
	ValidationWindowHours       pulumi.IntPtrOutput                                         `pulumi:"validationWindowHours"`
}

// NewRestoreTestingSelection registers a new resource with the given unique name, arguments, and options.
func NewRestoreTestingSelection(ctx *pulumi.Context,
	name string, args *RestoreTestingSelectionArgs, opts ...pulumi.ResourceOption) (*RestoreTestingSelection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IamRoleArn == nil {
		return nil, errors.New("invalid value for required argument 'IamRoleArn'")
	}
	if args.ProtectedResourceType == nil {
		return nil, errors.New("invalid value for required argument 'ProtectedResourceType'")
	}
	if args.RestoreTestingPlanName == nil {
		return nil, errors.New("invalid value for required argument 'RestoreTestingPlanName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"protectedResourceType",
		"restoreTestingPlanName",
		"restoreTestingSelectionName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RestoreTestingSelection
	err := ctx.RegisterResource("aws-native:backup:RestoreTestingSelection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRestoreTestingSelection gets an existing RestoreTestingSelection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRestoreTestingSelection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RestoreTestingSelectionState, opts ...pulumi.ResourceOption) (*RestoreTestingSelection, error) {
	var resource RestoreTestingSelection
	err := ctx.ReadResource("aws-native:backup:RestoreTestingSelection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RestoreTestingSelection resources.
type restoreTestingSelectionState struct {
}

type RestoreTestingSelectionState struct {
}

func (RestoreTestingSelectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*restoreTestingSelectionState)(nil)).Elem()
}

type restoreTestingSelectionArgs struct {
	IamRoleArn                  string                                              `pulumi:"iamRoleArn"`
	ProtectedResourceArns       []string                                            `pulumi:"protectedResourceArns"`
	ProtectedResourceConditions *RestoreTestingSelectionProtectedResourceConditions `pulumi:"protectedResourceConditions"`
	ProtectedResourceType       string                                              `pulumi:"protectedResourceType"`
	RestoreMetadataOverrides    *RestoreTestingSelectionSensitiveStringMap          `pulumi:"restoreMetadataOverrides"`
	RestoreTestingPlanName      string                                              `pulumi:"restoreTestingPlanName"`
	RestoreTestingSelectionName *string                                             `pulumi:"restoreTestingSelectionName"`
	ValidationWindowHours       *int                                                `pulumi:"validationWindowHours"`
}

// The set of arguments for constructing a RestoreTestingSelection resource.
type RestoreTestingSelectionArgs struct {
	IamRoleArn                  pulumi.StringInput
	ProtectedResourceArns       pulumi.StringArrayInput
	ProtectedResourceConditions RestoreTestingSelectionProtectedResourceConditionsPtrInput
	ProtectedResourceType       pulumi.StringInput
	RestoreMetadataOverrides    RestoreTestingSelectionSensitiveStringMapPtrInput
	RestoreTestingPlanName      pulumi.StringInput
	RestoreTestingSelectionName pulumi.StringPtrInput
	ValidationWindowHours       pulumi.IntPtrInput
}

func (RestoreTestingSelectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*restoreTestingSelectionArgs)(nil)).Elem()
}

type RestoreTestingSelectionInput interface {
	pulumi.Input

	ToRestoreTestingSelectionOutput() RestoreTestingSelectionOutput
	ToRestoreTestingSelectionOutputWithContext(ctx context.Context) RestoreTestingSelectionOutput
}

func (*RestoreTestingSelection) ElementType() reflect.Type {
	return reflect.TypeOf((**RestoreTestingSelection)(nil)).Elem()
}

func (i *RestoreTestingSelection) ToRestoreTestingSelectionOutput() RestoreTestingSelectionOutput {
	return i.ToRestoreTestingSelectionOutputWithContext(context.Background())
}

func (i *RestoreTestingSelection) ToRestoreTestingSelectionOutputWithContext(ctx context.Context) RestoreTestingSelectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RestoreTestingSelectionOutput)
}

func (i *RestoreTestingSelection) ToOutput(ctx context.Context) pulumix.Output[*RestoreTestingSelection] {
	return pulumix.Output[*RestoreTestingSelection]{
		OutputState: i.ToRestoreTestingSelectionOutputWithContext(ctx).OutputState,
	}
}

type RestoreTestingSelectionOutput struct{ *pulumi.OutputState }

func (RestoreTestingSelectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RestoreTestingSelection)(nil)).Elem()
}

func (o RestoreTestingSelectionOutput) ToRestoreTestingSelectionOutput() RestoreTestingSelectionOutput {
	return o
}

func (o RestoreTestingSelectionOutput) ToRestoreTestingSelectionOutputWithContext(ctx context.Context) RestoreTestingSelectionOutput {
	return o
}

func (o RestoreTestingSelectionOutput) ToOutput(ctx context.Context) pulumix.Output[*RestoreTestingSelection] {
	return pulumix.Output[*RestoreTestingSelection]{
		OutputState: o.OutputState,
	}
}

func (o RestoreTestingSelectionOutput) IamRoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.StringOutput { return v.IamRoleArn }).(pulumi.StringOutput)
}

func (o RestoreTestingSelectionOutput) ProtectedResourceArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.StringArrayOutput { return v.ProtectedResourceArns }).(pulumi.StringArrayOutput)
}

func (o RestoreTestingSelectionOutput) ProtectedResourceConditions() RestoreTestingSelectionProtectedResourceConditionsPtrOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) RestoreTestingSelectionProtectedResourceConditionsPtrOutput {
		return v.ProtectedResourceConditions
	}).(RestoreTestingSelectionProtectedResourceConditionsPtrOutput)
}

func (o RestoreTestingSelectionOutput) ProtectedResourceType() pulumi.StringOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.StringOutput { return v.ProtectedResourceType }).(pulumi.StringOutput)
}

func (o RestoreTestingSelectionOutput) RestoreMetadataOverrides() RestoreTestingSelectionSensitiveStringMapPtrOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) RestoreTestingSelectionSensitiveStringMapPtrOutput {
		return v.RestoreMetadataOverrides
	}).(RestoreTestingSelectionSensitiveStringMapPtrOutput)
}

func (o RestoreTestingSelectionOutput) RestoreTestingPlanName() pulumi.StringOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.StringOutput { return v.RestoreTestingPlanName }).(pulumi.StringOutput)
}

func (o RestoreTestingSelectionOutput) RestoreTestingSelectionName() pulumi.StringOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.StringOutput { return v.RestoreTestingSelectionName }).(pulumi.StringOutput)
}

func (o RestoreTestingSelectionOutput) ValidationWindowHours() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *RestoreTestingSelection) pulumi.IntPtrOutput { return v.ValidationWindowHours }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RestoreTestingSelectionInput)(nil)).Elem(), &RestoreTestingSelection{})
	pulumi.RegisterOutputType(RestoreTestingSelectionOutput{})
}
