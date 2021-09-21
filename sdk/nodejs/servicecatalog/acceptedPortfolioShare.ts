// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::AcceptedPortfolioShare
 *
 * @deprecated AcceptedPortfolioShare is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class AcceptedPortfolioShare extends pulumi.CustomResource {
    /**
     * Get an existing AcceptedPortfolioShare resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AcceptedPortfolioShare {
        pulumi.log.warn("AcceptedPortfolioShare is deprecated: AcceptedPortfolioShare is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new AcceptedPortfolioShare(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:servicecatalog:AcceptedPortfolioShare';

    /**
     * Returns true if the given object is an instance of AcceptedPortfolioShare.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AcceptedPortfolioShare {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AcceptedPortfolioShare.__pulumiType;
    }

    public readonly acceptLanguage!: pulumi.Output<string | undefined>;
    public readonly portfolioId!: pulumi.Output<string>;

    /**
     * Create a AcceptedPortfolioShare resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated AcceptedPortfolioShare is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: AcceptedPortfolioShareArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("AcceptedPortfolioShare is deprecated: AcceptedPortfolioShare is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.portfolioId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'portfolioId'");
            }
            inputs["acceptLanguage"] = args ? args.acceptLanguage : undefined;
            inputs["portfolioId"] = args ? args.portfolioId : undefined;
        } else {
            inputs["acceptLanguage"] = undefined /*out*/;
            inputs["portfolioId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(AcceptedPortfolioShare.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a AcceptedPortfolioShare resource.
 */
export interface AcceptedPortfolioShareArgs {
    acceptLanguage?: pulumi.Input<string>;
    portfolioId: pulumi.Input<string>;
}
