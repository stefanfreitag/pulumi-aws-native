// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::WorkSpaces::Workspace
 *
 * @deprecated Workspace is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Workspace {
        pulumi.log.warn("Workspace is deprecated: Workspace is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Workspace(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:workspaces:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    public readonly bundleId!: pulumi.Output<string>;
    public readonly directoryId!: pulumi.Output<string>;
    public readonly rootVolumeEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    public readonly tags!: pulumi.Output<outputs.workspaces.WorkspaceTag[] | undefined>;
    public readonly userName!: pulumi.Output<string>;
    public readonly userVolumeEncryptionEnabled!: pulumi.Output<boolean | undefined>;
    public readonly volumeEncryptionKey!: pulumi.Output<string | undefined>;
    public readonly workspaceProperties!: pulumi.Output<outputs.workspaces.WorkspaceWorkspaceProperties | undefined>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Workspace is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Workspace is deprecated: Workspace is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.bundleId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bundleId'");
            }
            if ((!args || args.directoryId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'directoryId'");
            }
            if ((!args || args.userName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userName'");
            }
            inputs["bundleId"] = args ? args.bundleId : undefined;
            inputs["directoryId"] = args ? args.directoryId : undefined;
            inputs["rootVolumeEncryptionEnabled"] = args ? args.rootVolumeEncryptionEnabled : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userName"] = args ? args.userName : undefined;
            inputs["userVolumeEncryptionEnabled"] = args ? args.userVolumeEncryptionEnabled : undefined;
            inputs["volumeEncryptionKey"] = args ? args.volumeEncryptionKey : undefined;
            inputs["workspaceProperties"] = args ? args.workspaceProperties : undefined;
        } else {
            inputs["bundleId"] = undefined /*out*/;
            inputs["directoryId"] = undefined /*out*/;
            inputs["rootVolumeEncryptionEnabled"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["userName"] = undefined /*out*/;
            inputs["userVolumeEncryptionEnabled"] = undefined /*out*/;
            inputs["volumeEncryptionKey"] = undefined /*out*/;
            inputs["workspaceProperties"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Workspace.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    bundleId: pulumi.Input<string>;
    directoryId: pulumi.Input<string>;
    rootVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    tags?: pulumi.Input<pulumi.Input<inputs.workspaces.WorkspaceTagArgs>[]>;
    userName: pulumi.Input<string>;
    userVolumeEncryptionEnabled?: pulumi.Input<boolean>;
    volumeEncryptionKey?: pulumi.Input<string>;
    workspaceProperties?: pulumi.Input<inputs.workspaces.WorkspaceWorkspacePropertiesArgs>;
}
