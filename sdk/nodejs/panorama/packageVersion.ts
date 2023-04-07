// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Schema for PackageVersion Resource Type
 */
export class PackageVersion extends pulumi.CustomResource {
    /**
     * Get an existing PackageVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PackageVersion {
        return new PackageVersion(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:panorama:PackageVersion';

    /**
     * Returns true if the given object is an instance of PackageVersion.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PackageVersion {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PackageVersion.__pulumiType;
    }

    public /*out*/ readonly isLatestPatch!: pulumi.Output<boolean>;
    public readonly markLatest!: pulumi.Output<boolean | undefined>;
    public readonly ownerAccount!: pulumi.Output<string | undefined>;
    public /*out*/ readonly packageArn!: pulumi.Output<string>;
    public readonly packageId!: pulumi.Output<string>;
    public /*out*/ readonly packageName!: pulumi.Output<string>;
    public readonly packageVersion!: pulumi.Output<string>;
    public readonly patchVersion!: pulumi.Output<string>;
    public /*out*/ readonly registeredTime!: pulumi.Output<number>;
    public /*out*/ readonly status!: pulumi.Output<enums.panorama.PackageVersionStatus>;
    public /*out*/ readonly statusDescription!: pulumi.Output<string>;
    public readonly updatedLatestPatchVersion!: pulumi.Output<string | undefined>;

    /**
     * Create a PackageVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PackageVersionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.packageId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'packageId'");
            }
            if ((!args || args.packageVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'packageVersion'");
            }
            if ((!args || args.patchVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'patchVersion'");
            }
            resourceInputs["markLatest"] = args ? args.markLatest : undefined;
            resourceInputs["ownerAccount"] = args ? args.ownerAccount : undefined;
            resourceInputs["packageId"] = args ? args.packageId : undefined;
            resourceInputs["packageVersion"] = args ? args.packageVersion : undefined;
            resourceInputs["patchVersion"] = args ? args.patchVersion : undefined;
            resourceInputs["updatedLatestPatchVersion"] = args ? args.updatedLatestPatchVersion : undefined;
            resourceInputs["isLatestPatch"] = undefined /*out*/;
            resourceInputs["packageArn"] = undefined /*out*/;
            resourceInputs["packageName"] = undefined /*out*/;
            resourceInputs["registeredTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusDescription"] = undefined /*out*/;
        } else {
            resourceInputs["isLatestPatch"] = undefined /*out*/;
            resourceInputs["markLatest"] = undefined /*out*/;
            resourceInputs["ownerAccount"] = undefined /*out*/;
            resourceInputs["packageArn"] = undefined /*out*/;
            resourceInputs["packageId"] = undefined /*out*/;
            resourceInputs["packageName"] = undefined /*out*/;
            resourceInputs["packageVersion"] = undefined /*out*/;
            resourceInputs["patchVersion"] = undefined /*out*/;
            resourceInputs["registeredTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusDescription"] = undefined /*out*/;
            resourceInputs["updatedLatestPatchVersion"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PackageVersion.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PackageVersion resource.
 */
export interface PackageVersionArgs {
    markLatest?: pulumi.Input<boolean>;
    ownerAccount?: pulumi.Input<string>;
    packageId: pulumi.Input<string>;
    packageVersion: pulumi.Input<string>;
    patchVersion: pulumi.Input<string>;
    updatedLatestPatchVersion?: pulumi.Input<string>;
}
