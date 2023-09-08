// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package workspacesweb

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::WorkSpacesWeb::UserSettings Resource Type
type UserSettings struct {
	pulumi.CustomResourceState

	AssociatedPortalArns           pulumi.StringArrayOutput      `pulumi:"associatedPortalArns"`
	CopyAllowed                    UserSettingsEnabledTypeOutput `pulumi:"copyAllowed"`
	DisconnectTimeoutInMinutes     pulumi.Float64PtrOutput       `pulumi:"disconnectTimeoutInMinutes"`
	DownloadAllowed                UserSettingsEnabledTypeOutput `pulumi:"downloadAllowed"`
	IdleDisconnectTimeoutInMinutes pulumi.Float64PtrOutput       `pulumi:"idleDisconnectTimeoutInMinutes"`
	PasteAllowed                   UserSettingsEnabledTypeOutput `pulumi:"pasteAllowed"`
	PrintAllowed                   UserSettingsEnabledTypeOutput `pulumi:"printAllowed"`
	Tags                           UserSettingsTagArrayOutput    `pulumi:"tags"`
	UploadAllowed                  UserSettingsEnabledTypeOutput `pulumi:"uploadAllowed"`
	UserSettingsArn                pulumi.StringOutput           `pulumi:"userSettingsArn"`
}

// NewUserSettings registers a new resource with the given unique name, arguments, and options.
func NewUserSettings(ctx *pulumi.Context,
	name string, args *UserSettingsArgs, opts ...pulumi.ResourceOption) (*UserSettings, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CopyAllowed == nil {
		return nil, errors.New("invalid value for required argument 'CopyAllowed'")
	}
	if args.DownloadAllowed == nil {
		return nil, errors.New("invalid value for required argument 'DownloadAllowed'")
	}
	if args.PasteAllowed == nil {
		return nil, errors.New("invalid value for required argument 'PasteAllowed'")
	}
	if args.PrintAllowed == nil {
		return nil, errors.New("invalid value for required argument 'PrintAllowed'")
	}
	if args.UploadAllowed == nil {
		return nil, errors.New("invalid value for required argument 'UploadAllowed'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource UserSettings
	err := ctx.RegisterResource("aws-native:workspacesweb:UserSettings", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserSettings gets an existing UserSettings resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserSettings(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserSettingsState, opts ...pulumi.ResourceOption) (*UserSettings, error) {
	var resource UserSettings
	err := ctx.ReadResource("aws-native:workspacesweb:UserSettings", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserSettings resources.
type userSettingsState struct {
}

type UserSettingsState struct {
}

func (UserSettingsState) ElementType() reflect.Type {
	return reflect.TypeOf((*userSettingsState)(nil)).Elem()
}

type userSettingsArgs struct {
	CopyAllowed                    UserSettingsEnabledType `pulumi:"copyAllowed"`
	DisconnectTimeoutInMinutes     *float64                `pulumi:"disconnectTimeoutInMinutes"`
	DownloadAllowed                UserSettingsEnabledType `pulumi:"downloadAllowed"`
	IdleDisconnectTimeoutInMinutes *float64                `pulumi:"idleDisconnectTimeoutInMinutes"`
	PasteAllowed                   UserSettingsEnabledType `pulumi:"pasteAllowed"`
	PrintAllowed                   UserSettingsEnabledType `pulumi:"printAllowed"`
	Tags                           []UserSettingsTag       `pulumi:"tags"`
	UploadAllowed                  UserSettingsEnabledType `pulumi:"uploadAllowed"`
}

// The set of arguments for constructing a UserSettings resource.
type UserSettingsArgs struct {
	CopyAllowed                    UserSettingsEnabledTypeInput
	DisconnectTimeoutInMinutes     pulumi.Float64PtrInput
	DownloadAllowed                UserSettingsEnabledTypeInput
	IdleDisconnectTimeoutInMinutes pulumi.Float64PtrInput
	PasteAllowed                   UserSettingsEnabledTypeInput
	PrintAllowed                   UserSettingsEnabledTypeInput
	Tags                           UserSettingsTagArrayInput
	UploadAllowed                  UserSettingsEnabledTypeInput
}

func (UserSettingsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userSettingsArgs)(nil)).Elem()
}

type UserSettingsInput interface {
	pulumi.Input

	ToUserSettingsOutput() UserSettingsOutput
	ToUserSettingsOutputWithContext(ctx context.Context) UserSettingsOutput
}

func (*UserSettings) ElementType() reflect.Type {
	return reflect.TypeOf((**UserSettings)(nil)).Elem()
}

func (i *UserSettings) ToUserSettingsOutput() UserSettingsOutput {
	return i.ToUserSettingsOutputWithContext(context.Background())
}

func (i *UserSettings) ToUserSettingsOutputWithContext(ctx context.Context) UserSettingsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserSettingsOutput)
}

func (i *UserSettings) ToOutput(ctx context.Context) pulumix.Output[*UserSettings] {
	return pulumix.Output[*UserSettings]{
		OutputState: i.ToUserSettingsOutputWithContext(ctx).OutputState,
	}
}

type UserSettingsOutput struct{ *pulumi.OutputState }

func (UserSettingsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserSettings)(nil)).Elem()
}

func (o UserSettingsOutput) ToUserSettingsOutput() UserSettingsOutput {
	return o
}

func (o UserSettingsOutput) ToUserSettingsOutputWithContext(ctx context.Context) UserSettingsOutput {
	return o
}

func (o UserSettingsOutput) ToOutput(ctx context.Context) pulumix.Output[*UserSettings] {
	return pulumix.Output[*UserSettings]{
		OutputState: o.OutputState,
	}
}

func (o UserSettingsOutput) AssociatedPortalArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *UserSettings) pulumi.StringArrayOutput { return v.AssociatedPortalArns }).(pulumi.StringArrayOutput)
}

func (o UserSettingsOutput) CopyAllowed() UserSettingsEnabledTypeOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsEnabledTypeOutput { return v.CopyAllowed }).(UserSettingsEnabledTypeOutput)
}

func (o UserSettingsOutput) DisconnectTimeoutInMinutes() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *UserSettings) pulumi.Float64PtrOutput { return v.DisconnectTimeoutInMinutes }).(pulumi.Float64PtrOutput)
}

func (o UserSettingsOutput) DownloadAllowed() UserSettingsEnabledTypeOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsEnabledTypeOutput { return v.DownloadAllowed }).(UserSettingsEnabledTypeOutput)
}

func (o UserSettingsOutput) IdleDisconnectTimeoutInMinutes() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *UserSettings) pulumi.Float64PtrOutput { return v.IdleDisconnectTimeoutInMinutes }).(pulumi.Float64PtrOutput)
}

func (o UserSettingsOutput) PasteAllowed() UserSettingsEnabledTypeOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsEnabledTypeOutput { return v.PasteAllowed }).(UserSettingsEnabledTypeOutput)
}

func (o UserSettingsOutput) PrintAllowed() UserSettingsEnabledTypeOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsEnabledTypeOutput { return v.PrintAllowed }).(UserSettingsEnabledTypeOutput)
}

func (o UserSettingsOutput) Tags() UserSettingsTagArrayOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsTagArrayOutput { return v.Tags }).(UserSettingsTagArrayOutput)
}

func (o UserSettingsOutput) UploadAllowed() UserSettingsEnabledTypeOutput {
	return o.ApplyT(func(v *UserSettings) UserSettingsEnabledTypeOutput { return v.UploadAllowed }).(UserSettingsEnabledTypeOutput)
}

func (o UserSettingsOutput) UserSettingsArn() pulumi.StringOutput {
	return o.ApplyT(func(v *UserSettings) pulumi.StringOutput { return v.UserSettingsArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserSettingsInput)(nil)).Elem(), &UserSettings{})
	pulumi.RegisterOutputType(UserSettingsOutput{})
}
