// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lakeformation

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::LakeFormation::DataLakeSettings
func LookupDataLakeSettings(ctx *pulumi.Context, args *LookupDataLakeSettingsArgs, opts ...pulumi.InvokeOption) (*LookupDataLakeSettingsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataLakeSettingsResult
	err := ctx.Invoke("aws-native:lakeformation:getDataLakeSettings", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataLakeSettingsArgs struct {
	Id string `pulumi:"id"`
}

type LookupDataLakeSettingsResult struct {
	Admins                           *DataLakeSettingsAdmins                           `pulumi:"admins"`
	AllowExternalDataFiltering       *bool                                             `pulumi:"allowExternalDataFiltering"`
	AllowFullTableExternalDataAccess *bool                                             `pulumi:"allowFullTableExternalDataAccess"`
	AuthorizedSessionTagValueList    []string                                          `pulumi:"authorizedSessionTagValueList"`
	CreateDatabaseDefaultPermissions *DataLakeSettingsCreateDatabaseDefaultPermissions `pulumi:"createDatabaseDefaultPermissions"`
	CreateTableDefaultPermissions    *DataLakeSettingsCreateTableDefaultPermissions    `pulumi:"createTableDefaultPermissions"`
	ExternalDataFilteringAllowList   *DataLakeSettingsExternalDataFilteringAllowList   `pulumi:"externalDataFilteringAllowList"`
	Id                               *string                                           `pulumi:"id"`
	MutationType                     *string                                           `pulumi:"mutationType"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::LakeFormation::DataLakeSettings` for more information about the expected schema for this property.
	Parameters            interface{} `pulumi:"parameters"`
	TrustedResourceOwners []string    `pulumi:"trustedResourceOwners"`
}

func LookupDataLakeSettingsOutput(ctx *pulumi.Context, args LookupDataLakeSettingsOutputArgs, opts ...pulumi.InvokeOption) LookupDataLakeSettingsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataLakeSettingsResult, error) {
			args := v.(LookupDataLakeSettingsArgs)
			r, err := LookupDataLakeSettings(ctx, &args, opts...)
			var s LookupDataLakeSettingsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataLakeSettingsResultOutput)
}

type LookupDataLakeSettingsOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDataLakeSettingsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataLakeSettingsArgs)(nil)).Elem()
}

type LookupDataLakeSettingsResultOutput struct{ *pulumi.OutputState }

func (LookupDataLakeSettingsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataLakeSettingsResult)(nil)).Elem()
}

func (o LookupDataLakeSettingsResultOutput) ToLookupDataLakeSettingsResultOutput() LookupDataLakeSettingsResultOutput {
	return o
}

func (o LookupDataLakeSettingsResultOutput) ToLookupDataLakeSettingsResultOutputWithContext(ctx context.Context) LookupDataLakeSettingsResultOutput {
	return o
}

func (o LookupDataLakeSettingsResultOutput) Admins() DataLakeSettingsAdminsPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *DataLakeSettingsAdmins { return v.Admins }).(DataLakeSettingsAdminsPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) AllowExternalDataFiltering() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *bool { return v.AllowExternalDataFiltering }).(pulumi.BoolPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) AllowFullTableExternalDataAccess() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *bool { return v.AllowFullTableExternalDataAccess }).(pulumi.BoolPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) AuthorizedSessionTagValueList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) []string { return v.AuthorizedSessionTagValueList }).(pulumi.StringArrayOutput)
}

func (o LookupDataLakeSettingsResultOutput) CreateDatabaseDefaultPermissions() DataLakeSettingsCreateDatabaseDefaultPermissionsPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *DataLakeSettingsCreateDatabaseDefaultPermissions {
		return v.CreateDatabaseDefaultPermissions
	}).(DataLakeSettingsCreateDatabaseDefaultPermissionsPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) CreateTableDefaultPermissions() DataLakeSettingsCreateTableDefaultPermissionsPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *DataLakeSettingsCreateTableDefaultPermissions {
		return v.CreateTableDefaultPermissions
	}).(DataLakeSettingsCreateTableDefaultPermissionsPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) ExternalDataFilteringAllowList() DataLakeSettingsExternalDataFilteringAllowListPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *DataLakeSettingsExternalDataFilteringAllowList {
		return v.ExternalDataFilteringAllowList
	}).(DataLakeSettingsExternalDataFilteringAllowListPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDataLakeSettingsResultOutput) MutationType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) *string { return v.MutationType }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::LakeFormation::DataLakeSettings` for more information about the expected schema for this property.
func (o LookupDataLakeSettingsResultOutput) Parameters() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) interface{} { return v.Parameters }).(pulumi.AnyOutput)
}

func (o LookupDataLakeSettingsResultOutput) TrustedResourceOwners() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDataLakeSettingsResult) []string { return v.TrustedResourceOwners }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataLakeSettingsResultOutput{})
}
