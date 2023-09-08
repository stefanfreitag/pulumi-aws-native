// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package workspaces

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::WorkSpaces::Workspace
func LookupWorkspace(ctx *pulumi.Context, args *LookupWorkspaceArgs, opts ...pulumi.InvokeOption) (*LookupWorkspaceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWorkspaceResult
	err := ctx.Invoke("aws-native:workspaces:getWorkspace", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupWorkspaceArgs struct {
	Id string `pulumi:"id"`
}

type LookupWorkspaceResult struct {
	BundleId                    *string              `pulumi:"bundleId"`
	DirectoryId                 *string              `pulumi:"directoryId"`
	Id                          *string              `pulumi:"id"`
	RootVolumeEncryptionEnabled *bool                `pulumi:"rootVolumeEncryptionEnabled"`
	Tags                        []WorkspaceTag       `pulumi:"tags"`
	UserVolumeEncryptionEnabled *bool                `pulumi:"userVolumeEncryptionEnabled"`
	VolumeEncryptionKey         *string              `pulumi:"volumeEncryptionKey"`
	WorkspaceProperties         *WorkspaceProperties `pulumi:"workspaceProperties"`
}

func LookupWorkspaceOutput(ctx *pulumi.Context, args LookupWorkspaceOutputArgs, opts ...pulumi.InvokeOption) LookupWorkspaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWorkspaceResult, error) {
			args := v.(LookupWorkspaceArgs)
			r, err := LookupWorkspace(ctx, &args, opts...)
			var s LookupWorkspaceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWorkspaceResultOutput)
}

type LookupWorkspaceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupWorkspaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkspaceArgs)(nil)).Elem()
}

type LookupWorkspaceResultOutput struct{ *pulumi.OutputState }

func (LookupWorkspaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWorkspaceResult)(nil)).Elem()
}

func (o LookupWorkspaceResultOutput) ToLookupWorkspaceResultOutput() LookupWorkspaceResultOutput {
	return o
}

func (o LookupWorkspaceResultOutput) ToLookupWorkspaceResultOutputWithContext(ctx context.Context) LookupWorkspaceResultOutput {
	return o
}

func (o LookupWorkspaceResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupWorkspaceResult] {
	return pulumix.Output[LookupWorkspaceResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupWorkspaceResultOutput) BundleId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *string { return v.BundleId }).(pulumi.StringPtrOutput)
}

func (o LookupWorkspaceResultOutput) DirectoryId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *string { return v.DirectoryId }).(pulumi.StringPtrOutput)
}

func (o LookupWorkspaceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupWorkspaceResultOutput) RootVolumeEncryptionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *bool { return v.RootVolumeEncryptionEnabled }).(pulumi.BoolPtrOutput)
}

func (o LookupWorkspaceResultOutput) Tags() WorkspaceTagArrayOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) []WorkspaceTag { return v.Tags }).(WorkspaceTagArrayOutput)
}

func (o LookupWorkspaceResultOutput) UserVolumeEncryptionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *bool { return v.UserVolumeEncryptionEnabled }).(pulumi.BoolPtrOutput)
}

func (o LookupWorkspaceResultOutput) VolumeEncryptionKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *string { return v.VolumeEncryptionKey }).(pulumi.StringPtrOutput)
}

func (o LookupWorkspaceResultOutput) WorkspaceProperties() WorkspacePropertiesPtrOutput {
	return o.ApplyT(func(v LookupWorkspaceResult) *WorkspaceProperties { return v.WorkspaceProperties }).(WorkspacePropertiesPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWorkspaceResultOutput{})
}
